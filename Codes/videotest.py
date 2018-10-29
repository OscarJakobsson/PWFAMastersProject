

from matplotlib import pyplot as plt
import numpy as np
import cv2
import scipy.io as sio
import os
import scipy.misc
import csv




def video():

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')      #output-video codec

    out = cv2.VideoWriter('Energy_linear_100pC.mp4',fourcc, 20.0, (1024-54+1024-654+1024-654,914))     #full size (640,586)





    for i in range (0,201):
        img= np.zeros(shape=(914,1024-54+1024-654+1024-654,3),dtype=np.uint8)     
        name2='test_run_quasilinear/visit00%d.png'%i
        name1='test_run_nonlinear/test_run_nonlinear/visit00%d.png'%i
        name3='test_run_linear/test_run_linear/visit00%d.png'%i

        if (i<10):
            name2='test_run_quasilinear/visit000%d.png'%i
            name1='test_run_nonlinear/test_run_nonlinear/visit000%d.png'%i
            name3='test_run_linear/test_run_linear/visit000%d.png'%i
        if (i>99):
            name2='test_run_quasilinear/visit0%d.png'%i
            name1='test_run_nonlinear/test_run_nonlinear/visit0%d.png'%i
            name3='test_run_linear/test_run_linear/visit0%d.png'%i
        print(name1)

        if os.path.exists(name2):
            frame1=cv2.imread(name1)
            frame2=cv2.imread(name2)
            frame3=cv2.imread(name3)    

            for i in range(0,frame1.shape[0]):  #(0,586):
                for j in range(0,frame1.shape[1]-52):  #(0,640):
                    for k in range(0,frame1.shape[2]):  #(0,640):

                        img[i,j,k]=frame1[i,j,k]

            #plt.imsave("aabc.png"% img,cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            for i in range(0,frame1.shape[0]):  #(0,586):
                for j in range(0,frame1.shape[1]-600):  #(0,640):
                    for k in range(0,frame1.shape[2]):  #(0,640):

                        img[i,j+1024-54,k]=frame2[i,j+600,k]
            for i in range(0,frame1.shape[0]):  #(0,586):
                for j in range(0,frame1.shape[1]-654):  #(0,640):
                    for k in range(0,frame1.shape[2]):  #(0,640):

                        img[i,j+1024-54+1024-654,k]=frame3[i,j+600,k]

            for i in range(0,frame1.shape[0]):  #(0,586):
                    for k in range(0,frame1.shape[2]):  #(0,640):
                        img[i,1024-54+1024-654,k]=0
                        img[i,1024-54,k]=0

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img,'n_p=0.1n_b',(760,100), font, 1.0,(0,0,0),2)
            cv2.putText(img,'n_p=n_b',(800+380,100), font, 1.0,(0,0,0),2)
            cv2.putText(img,'n_p=10n_b',(800+710,100), font, 1.0,(0,0,0),2)

            plt.imsave("screenshot.png"% img,cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            if i<=1000:
                
        
                # write the flipped frame
                out.write(img)
        
                #cv2.imshow('img',img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break    
        
            
        
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        

    out.release()

video()
 
