'''
ECE276A WI19 HW1
Blue Barrel Detector
'''

import os, cv2
from skimage.measure import label, regionprops
from prob import get_pic1
import numpy as np
import skimage
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

class BarrelDetector():
    def __init__(self):
        '''
        Initilize your blue barrel detector with the attributes you need
        eg. parameters of your classifier
        
        '''
        #raise NotImplementedError
        def segment_image(img):
            return mask_img
        def get_bounding_box(img):
            return boxes

    def segment_image(self, img):
        '''
        Calculate the segmented image using a classifier
        eg. Single Gaussian, Gaussian Mixture, or Logistic Regression
        call other functions in this class if needed

        Inputs:
        img - original image
        Outputs:
        mask_img - a binary image with 1 if the pixel in the original image is blue and 0 otherwise
        '''
        # YOUR CODE HERE

        test_img=img
        imgg=cv2.cvtColor(test_img,cv2.COLOR_RGB2BGR)
        imgy=cv2.cvtColor(test_img,cv2.COLOR_RGB2YCR_CB)
        mask_img = get_pic1(imgy)    
        #raise NotImplementedError
        return mask_img

    def get_bounding_box(self, img):
        '''
        Find the bounding box of the blue barrel
        call other functions in this class if needed

        Inputs:
        img - original image
        Outputs:
        boxes - a list of lists of bounding boxes. Each nested list is a bounding box in the form of [x1, y1, x2, y2] 
        where (x1, y1) and (x2, y2) are the top left and bottom right coordinate respectively. The order of bounding boxes in the list
        is from left to right in the image.
     
        Our solution uses xy-coordinate instead of rc-coordinate. More information: http://scikitimage.org/docs/dev/user_guide/numpy_images.html#coordinate-conventions
           '''
        
        # YOUR CODE HERE
        seg_img = self.segment_image(img)
        image = seg_img

        # apply threshold
        thresh = threshold_otsu(image)
        bw = closing(image > thresh, square(3))

        # remove artifacts connected to image border
        cleared = clear_border(bw)

        # label image regions
        label_image = label(cleared)
        boxes = []
        for region in regionprops(label_image):
            # take regions with large enough areas
            if region.area >= 2000:
                # draw rectangle around segmented coins
                minr, minc, maxr, maxc = region.bbox
                box = [minc,minr,maxc,maxr]
                boxes.append(box)

    


        
        #raise NotImplementedError
        return boxes


if __name__ == '__main__':
    
    folder = "trainset"
    my_detector = BarrelDetector()
    for filename in os.listdir(folder):
        # read one test image
        img = cv2.imread(os.path.join(folder,filename))
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

       
        #Display results:
        #(1) Segmented images
        # mask_img = my_detector.segment_image(img)
        #(2) Barrel bounding box
        #    boxes = my_detector.get_bounding_box(img)
        #The autograder checks your answers to the functions segment_image() and get_bounding_box()
        #Make sure your code runs as expected on the testset before submitting to Gradescope
          
