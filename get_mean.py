import numpy as np
import math
import pickle
import pylab as pl
import cv2

def get_gmean(my_blue):
        #analyzing blue color data by finding gaussian mean and covernce
        

        blue= pickle.load(my_blue)
        my_blue.close()
        blue_color = np.matrix(blue)
        n1 = len(blue[0])
        n2 = len(blue[1])
        n3 = len(blue[2])
        Red_mean = sum(blue[0]) / n1
        Green_mean = sum(blue[1]) / n2
        Blue_mean = sum(blue[2]) / n3
        color_mean = [[Red_mean], [Green_mean], [Blue_mean]]

        k = blue_color.shape
        color_cov = sum([(blue_color[:, i] - color_mean) * (blue_color[:, i] - color_mean).T for i in range(k[1])]) / (k[1] - 1)
        print(color_mean)
        print(color_cov)
        return [color_mean, color_cov]