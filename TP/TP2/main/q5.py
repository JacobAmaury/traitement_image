import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *


def run_q5():
    
    print("5: Histogramme equalisation")
    print("As we can see the histogramme equalized take the full range of gray lvl. The third histogramme took all the range of gray lvl and all the bins have the same height.")
    path_lena = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Lena.jpg" 
    image_Lena = open_image(path_lena, "L")
    
    histo_base, bin = np.histogram(image_Lena, 255  )
    image_Lena_equa = equa_histo(image_Lena)
    histo_equ, bin = np.histogram(image_Lena_equa, 255)
    image_Lena_equa_exa = equlisation_exact(image_Lena)
    
    histo_equ_exa, bin = np.histogram(image_Lena_equa_exa, 255)
    
    plt.subplot(2,3,1)
    plt.title("Base image")
    plt.imshow(image_Lena, cmap='grey')
    plt.subplot(2,3,2)
    plt.title("Histogramme equalized")
    plt.imshow(image_Lena_equa, cmap='grey')
    plt.subplot(2,3,3)
    plt.title("Exact histogramme equalisation")
    plt.imshow(image_Lena_equa_exa, cmap='grey')
    plt.subplot(2,3,4)
    plt.bar(bin[:-1], histo_base)
    plt.subplot(2,3,5)
    plt.bar(bin[:-1], histo_equ)
    plt.subplot(2,3,6)
    plt.bar(bin[:-1], histo_equ_exa)
    plt.show()
    
    