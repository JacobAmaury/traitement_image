#/*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 03102025 08:47:48     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random as rd

def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img

def conv_product(image, filter):

    height, width, channels = image.shape
    filter_height, filter_width = filter.shape
    to_border = int(filter_height/2)

    im_convo = np.zeros_like(image)

    #normalistion du filtre
    sum_coef = np.sum(filter)
    if sum_coef == 0: sum_coef = 1


    for c in range(channels):
        for y in range(to_border, height - to_border): #evite les effets de bord
            for x in range(to_border, width - to_border):
                #on récupere la fentre autour du point(x,y)
                conv = image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1, c]
                value = np.sum(conv * filter) / sum_coef #on fait la somme et on normalise

                val = int(value)
                if val < 0: val = 0
                elif val > 255: val = 255

                im_convo[y, x, c] = val

    return im_convo

def median(image, window_size):
    height, width, channels = image.shape
    to_border = int(window_size/2)

    im_convo = np.zeros_like(image)

    #normalistion du filtre
    sum_coef = np.sum(filter)
    if sum_coef == 0: sum_coef = 1


    for c in range(channels):
        for y in range(to_border, height - to_border): #evite les effets de bord
            for x in range(to_border, width - to_border):
                #on récupere la fentre autour du point(x,y)
                median = np.median(image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1, c])

                im_convo[y, x, c] = median

    return im_convo



def poivre_sel(image, prob):
    width, height, chanel = image.shape
    noisy_image = np.zeros_like(image)
    
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            random_value = rd.random()
            if(random_value < prob):
                noisy_image[x-1:x+1, y-1:y+1, :] = 255
            else:
                noisy_image[x-1:x+1, y-1:y+1, :] = image[x-1:x+1, y-1:y+1, :] 
            
            
            
    return noisy_image 

