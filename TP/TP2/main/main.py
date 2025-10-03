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

image_clown = open_image(path_clown,"L")
image_noisy_Lena = open_image(path_noisy_lena, "RGB")
image_Lena = open_image(path_lena)

filtered_clown(image_clown)


