import numpy as np
import math
import pickle
import pylab as pl
import cv2

def get_pic1(img):
    
    blue_mean = [[87.29005169978507], [151.77404216733981], [105.93964189436278]]
    blue_cov =  [[1824.53347041,  243.55688529, -344.88646151],
                 [ 243.55688529,  404.28644666, -372.05219782],
                 [-344.88646151, -372.05219782,  440.54099441]]
    brown_mean = [[86.24381677923898], [119.84258033828009], [138.57029366077515]]
    brown_cov = [[2134.00997358,  -50.84196195,   83.54663809],
                 [ -50.84196195,   45.02288385,  -50.06946494],
                 [  83.54663809,  -50.06946494,   93.34954267]]

    notblue_mean = [[95.00754377992128], [125.16153944832932], [130.74361690658282]]
    notblue_cov = [[ 2.77018283e+03, -2.01079684e+00, -5.61688059e+01],
                   [-2.01079684e+00,  7.75387975e+01, -8.00213911e+01],
                   [-5.61688059e+01, -8.00213911e+01,  2.08859592e+02]]

    yellow_mean = [[87.87716574750252], [117.89459458719868], [131.92219253045587]]

    yellow_cov = [[2012.81197337,  -36.17953438,   35.13296184],
                  [ -36.17953438,   98.78382497,  -54.96734897],
                  [  35.13296184,  -54.96734897,   72.73756765]]
    blue_cov_a=1/math.sqrt(((2*math.pi) **3) *abs(np.linalg.det(blue_cov)))
    brown_cov_a=1/math.sqrt(((2*math.pi) **3) *abs(np.linalg.det(brown_cov)))
    notblue_cov_a=1/math.sqrt(((2*math.pi) **3) *abs(np.linalg.det(notblue_cov)))
    yellow_cov_a=1/math.sqrt(((2*math.pi) **3) *abs(np.linalg.det(yellow_cov)))
    blue_b = np.linalg.inv(blue_cov)
    brown_b = np.linalg.inv(brown_cov)
    notblue_b=np.linalg.inv(notblue_cov)
    yellow_b=np.linalg.inv(yellow_cov)
    array = img[::10,::10,:]
    k = array[:, :, 0].shape
    pic = np.zeros((array.shape[0], array.shape[1]))
    P_blue=np.zeros([800,1200])
    P_brown=np.zeros([800,1200])
    P_notblue=np.zeros([800,1200])
    P_yellow=np.zeros([800,1200])

    for i in range(k[0]):
        for j in range(k[1]):
            color = [[array[i, j, 0]], [array[i, j, 1]], [array[i, j, 2]]]
            my_color=np.matrix(color)
        
            P_blue[i,j] =blue_cov_a*math.exp((-0.5)*(my_color - blue_mean).T *blue_b * (my_color - blue_mean))
            P_brown[i,j] =brown_cov_a*math.exp((-0.5)*(my_color - brown_mean).T *brown_b * (my_color - brown_mean))
            P_notblue[i,j] =notblue_cov_a*math.exp((-0.5)*(my_color - notblue_mean).T *notblue_b * (my_color - notblue_mean))
            P_yellow[i,j] =yellow_cov_a*math.exp((-0.5)*(my_color - yellow_mean).T *yellow_b * (my_color - yellow_mean))
            if max(P_blue[i,j],P_brown[i,j],P_notblue[i,j],P_yellow[i,j]) == P_blue[i,j]:
                pic[i,j]=1
            else:
                pic[i,j]=0
    pic = cv2.resize(pic,(1200,800))       
    return(pic)