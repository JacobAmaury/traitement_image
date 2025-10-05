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
path_flag = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/France.png"
path_mark = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Mark.png"
path_text_rest = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/texte_a_restaurer.png"

im_text_rest = open_image(path_text_rest, "L")
france_flag = open_image(path_flag)
image_mark = open_image(path_mark)
image_clown = open_image(path_clown,"L")
image_noisy_Lena = open_image(path_noisy_lena)
image_Lena = open_image(path_lena)
image_noise = open_image(path_noise, "L")

#filtered_clown(image_clown)
#filtered_noise(image_noise)


# Lena_de_noise = median(image_noisy_Lena, 4)
# Lena_de_noise_equa = equlisation_exact(Lena_de_noise)
# histo_Lena,bin_lena = np.histogram(Lena_de_noise_equa, 255)

# plt.subplot(1,2,1)
# plt.bar(bin_lena[:-1],histo_Lena)
# plt.subplot(1,2,2)
# plt.imshow(Lena_de_noise_equa)



# Mark_france = picture_flag(image_mark, france_flag)

# plt.imshow(Mark_france)
im_text_rest_equa = equa_histo(im_text_rest)
plt.imshow(im_text_rest, cmap="gray")
plt.show()


