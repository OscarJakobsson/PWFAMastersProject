

from matplotlib import pyplot as plt
import numpy as np
import cv2
import scipy.io as sio
import os
import scipy.misc
import csv




for i in range (3,4):
    #img= np.zeros(shape=(914,1024-54+1024-654+1024-654,3),dtype=np.uint8)     
    name2='bunch/visit00%d.png'%i
    name1='plasma/visit00%d.png'%i

    if (i<10):
        name2='bunch/visit000%d.png'%i
        name1='plasma/visit000%d.png'%i
    if (i>99):
        name2='bunch/visit0%d.png'%i
        name1='plasma/visit0%d.png'%i
    
    name='frame%d.png'%i
    print(name)
    if os.path.exists(name2):
        frame1=cv2.imread(name1)
        frame2=cv2.imread(name2)  

        for i in range(0,frame2.shape[0]):  #(0,586):
            for j in range(0,frame2.shape[1]):  #(0,640):
                for k in range(0,frame2.shape[2]):  #(0,640):
                    if (frame2[i,j,2]>60 and frame2[i,j,2]!=0 and frame2[i,j,2]!=0 ):
                        frame1[i,j,k]=frame2[i,j,k]

        plt.imsave("screenshot.pdf"% frame1,cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
        
        plt.imsave(name% frame1,cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))

