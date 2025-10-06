import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *


def run_q2():
    print("Question 2: Periodic noise filtering ")
    print("As we can see in the middle pictures I have masked some points. These points correspond to the periodic motif so if we mask them and do the ifft the periodic modif desappear")
    print("Do not forget to close the matplotlib window in order to go back to the menu")
    path_clown = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/clown.tif"
    path_noise = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/noise.tif"
    image_clown = open_image(path_clown, "L")
    image_noise = open_image(path_noise, "L")
    
    
    clown_fft = np.fft.fft2(image_clown) 
    clown_fft_shift = np.fft.fftshift(clown_fft)
    clown_fft_shift[75:95, 10:30] = 0
    clown_fft_shift[30:50, 96:116] = 0
    clown_fft_shift[45:55, 35:45] = 0
    clown_fft_shift[70:80, 80:90] = 0
    clown_shift2 = np.fft.fftshift(clown_fft_shift)
    clown_recon = np.fft.ifft2(clown_shift2)
    
    
    noise_fft = np.fft.fft2(image_noise)
    noise_fft_shift = np.fft.fftshift(noise_fft)
    noise_fft_shift[124:129, :65] = 0
    noise_fft_shift[124:129, 185:] = 0
    noise_shift2 = np.fft.fftshift(noise_fft_shift)
    noise_recon = np.fft.ifft2(noise_shift2)
    
    

    plt.subplot(2,3,3)
    plt.imshow(np.real(clown_recon), cmap="gray")
    plt.axis("off")

    plt.subplot(2,3,2)
    plt.imshow(np.log(np.abs(clown_fft_shift)), cmap="gray")
    plt.axis("off")


    plt.subplot(2,3,1)
    plt.imshow(image_clown, cmap="gray")
    plt.axis("off")
    
    
    plt.subplot(2,3,6)
    plt.imshow(np.real(noise_recon), cmap="gray")
    plt.axis("off")

    plt.subplot(2,3,5)
    plt.imshow(np.log(np.abs(noise_fft_shift)), cmap="gray")
    plt.axis("off")


    plt.subplot(2,3,4)
    plt.imshow(image_noise, cmap="gray")
    plt.axis("off")

    plt.show()
    


    
