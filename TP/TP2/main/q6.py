import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

def run_q6():
    print("6: Restauration of printed document")
    print("I have tried many approaches, but this is the best solution I’ve found. First, I applied a threshold, then a median filter, and finally an erosion and a dilation.")
    path_text_rest = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/texte_a_restaurer.png"
    im_text_rest = open_image(path_text_rest, "L") 

    im_rest = thresholding(im_text_rest, 211)
    im_rest = median(im_rest, 2, "L") 
    im_rest = erosion(im_rest)
    im_rest = dilatation(im_rest)
    
    plt.subplot(1,2,1)
    plt.title("Base image")
    plt.imshow(im_text_rest, cmap="gray")
    plt.subplot(1,2,2)
    plt.title("Image restaured")
    plt.imshow(im_rest, cmap="gray")
    plt.show()
