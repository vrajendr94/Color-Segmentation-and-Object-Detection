import numpy as np
from roipoly import roipoly
import cv2
import pylab as pl
import os
import pickle
from skimage import measure
import matplotlib


# create image
my_pic=os.listdir('/Users/vaish/Desktop/img')
Blue_class=[[],[],[]]
blue_class_area=[]
matplotlib.use('TkAgg')

for img_file in my_pic:
     if img_file.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:
            img1 = cv2.imread(img_file)
            img2 = cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)



            # show the image
            pl.imshow(img2)
            pl.colorbar()
            pl.title("left click: line segment         right click: close region")

            # let user draw first ROI in red color
            ROI1 = roipoly(roicolor='r') #let user draw first ROI

            # show the image with the first ROI
            ROI1.displayROI()
            # show the image with ROI and their mean values


            a=ROI1.getMask(img1[:,:,0])
            pl.imshow(a)
            pl.show()
            positions=np.where(a == True)

            imgy=cv2.cvtColor(img1,cv2.COLOR_RGB2YCR_CB)

            red = imgy[:, :, 0]
            green = imgy[:, :, 1]
            blue = imgy[:, :, 2]

            B=blue[positions]
            R=red[positions]
            G=green[positions]
            Blue_class[0].extend(R.tolist())
            Blue_class[1].extend(G.tolist())
            Blue_class[2].extend(B.tolist())

            label_mask = measure.label(a)
            G_p = measure.regionprops(label_mask)
            blue_class_area.append(G_p[0].area)

            
    
                

my_blueclass = open('blueclass.pkl','wb')
pickle.dump(Blue_class,my_blueclass)
my_blueclass.close()


my_bluearea = open('bluearea.pkl', 'wb')
pickle.dump(blue_class_area, my_bluearea)
my_bluearea.close()




