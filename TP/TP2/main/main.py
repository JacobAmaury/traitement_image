#/*
# * Auteur : Jacob Amaury                 |\      _,,,---,,_
# * Date   : 03102025 08:49:38     ZZZzz  /,`.-'`'    -.  ;-;;,_
# *                                      |,4-  ) )-,_. ,\ (  `'-' 
# */                                    '---''(_/--'  `-'\_)


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

path_noisy_lena = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/noisy_Lena.png"
path_lena = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Lena.jpg"
path_clown = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/clown.tif"
path_noise = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/noise.tif"

image_clown = open_image(path_clown,"L")
image_noisy_Lena = open_image(path_noisy_lena)
image_Lena = open_image(path_lena)
image_noise = open_image(path_noise, "L")

#filtered_clown(image_clown)
#filtered_noise(image_noise)

Lena_de_noise = median(image_noisy_Lena, 4)
Lena_de_noise_equa = equa_histo(Lena_de_noise)
plt.subplot(1,2,1)
plt.imshow(Lena_de_noise)
plt.subplot(1,2,2)
plt.imshow(Lena_de_noise_equa)
plt.show()


