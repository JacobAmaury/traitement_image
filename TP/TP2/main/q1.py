import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

def run_q1(): 
    print("Question 1: median filter")
    print("As we can see the image on the left as been smoothed but we dont have any noise left.")
    print("The computation time is quite long (1min)")
    path_lena = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Lena.jpg" 
    image_Lena = open_image(path_lena)
    Lena_bruit = poivre_sel(image_Lena, 0.1)
    Lena_debruit = median(Lena_bruit, 3, "RGB")
    Lena_debruit = median(Lena_bruit, 5, "RGB")
    plt.subplot(1,3,1)
    plt.title("base image")
    plt.imshow(image_Lena)
    plt.subplot(1,3,2)
    plt.title("noisy image")
    plt.imshow(Lena_bruit)
    plt.subplot(1,3,3)
    plt.title("cleaned image")
    plt.imshow(Lena_debruit)
    plt.show()


