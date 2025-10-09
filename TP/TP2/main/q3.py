import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

def run_q3():
    print("Question 3: supression of noise")
    print("As we can see it works quite well in the image of mercury but on the second image we have to much noise so the cleaned image is too smooth.")
    print("Do not forget to close the matplotlib window in order to go back to the menu")
    path_mecury = "../Images_TP/mercury.tif"
    path_noisy_lena = "../Images_TP/noisy_Lena.png"
    
    im_mercury = open_image(path_mecury)
    im_noisy_lena = open_image(path_noisy_lena)
    
    im_mercury_clean = median(im_mercury, 3, "RGB")
    im_noisy_lena_clean = median(im_noisy_lena, 3, "RGB")
   
    
    plt.subplot(2,2,1)
    plt.title("Mercury image before cleaning")
    plt.imshow(im_mercury)
    plt.subplot(2,2,2)
    plt.title("Mecury image cleaned")
    plt.imshow(im_mercury_clean)
    plt.subplot(2,2,3)
    plt.title("Noisy Lena image")
    plt.imshow(im_noisy_lena)
    plt.subplot(2,2,4)
    plt.title("Cleaned noisy Lena")
    plt.imshow(im_noisy_lena_clean)
    plt.show()
    