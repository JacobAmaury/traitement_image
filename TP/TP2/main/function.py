#/*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 03102025 08:47:48     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random as rd
from skimage.transform import resize

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

    im_med = np.zeros_like(image)

    for c in range(channels):
        for y in range(to_border, height - to_border): #evite les effets de bord
            for x in range(to_border, width - to_border):
                #on récupere la fentre autour du point(x,y)
                median = np.median(image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1, c])

                im_med[y, x, c] = median

    return im_med



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

def fft_im(image):
    return np.fft.fft2(image)

def filtered_clown(image_clown):
    clown_fft = np.fft.fft2(image_clown) 
    clown_fft_shift = np.fft.fftshift(clown_fft)
    clown_fft_shift[75:95, 10:30] = 0
    clown_fft_shift[30:50, 96:116] = 0
    clown_fft_shift[45:55, 35:45] = 0
    clown_fft_shift[70:80, 80:90] = 0

    clown_shift2 = np.fft.fftshift(clown_fft_shift)
    clown_recon = np.fft.ifft2(clown_shift2)

    plt.figure(figsize=(12,6))

    plt.subplot(1,3,3)
    plt.imshow(np.real(clown_recon), cmap="gray")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(np.log(np.abs(clown_fft_shift)), cmap="gray")
    plt.axis("off")


    plt.subplot(1,3,1)
    plt.imshow(image_clown, cmap="gray")
    plt.axis("off")

    plt.show()



def filtered_noise(image_noice):
    noise_fft = np.fft.fft2(image_noice)
    noise_fft_shift = np.fft.fftshift(noise_fft)
    noise_fft_shift[124:129, :65] = 0
    noise_fft_shift[124:129, 185:] = 0
    noise_shift2 = np.fft.fftshift(noise_fft_shift)
    noise_recon = np.fft.ifft2(noise_shift2)

    plt.figure(figsize=(12,6))

    plt.subplot(1,3,3)
    plt.imshow(np.real(noise_recon), cmap="gray")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(np.log(np.abs(noise_fft_shift)), cmap="gray")
    plt.axis("off")


    plt.subplot(1,3,1)
    plt.imshow(image_noice, cmap="gray")
    plt.axis("off")

    plt.show()
    
def print_fft(image):
    fft = np.fft.fft2(image)
    fft_shift = np.fft.fftshift(fft)
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(np.log(np.abs(fft_shift)), cmap='gray')
    plt.show()
    

def crop_image(image_to_crop, dimensions):
    x, y, _ = image_to_crop.shape 
    center_x = x // 2
    center_y = y // 2
    
    crop_image = image_to_crop[
        center_x - dimensions[0]//2 : center_x + dimensions[0]//2,
        center_y-1 - dimensions[1]//2 : center_y + dimensions[1]//2]
    return crop_image 
    
    

#Ne fait pas exactement la bonne. Elle devrait changer la résolution de l'image pour l'adpter au drapeau
#Mais elle recadre 
def picture_flag(image, flag):
    image_crop = crop_image(image, flag.shape)
    image_flag = (image_crop + flag) / 2
    image_flag = np.clip(image_flag, 0, 255)
    
    return image_flag.astype(int)

    
def normalisation_histo(image):
    I_max = np.max(image)
    I_min = np.min(image)
    return (((image-I_min)/(I_max-I_min))*255).astype(int)


def histo_cumu(image):
    histo, bin = np.histogram(image, 256)
    histo_cumu = np.zeros_like(histo)
    for i in range(histo.shape[0]):
        histo_cumu[i] = np.sum(histo[:i+1])

    return histo_cumu
    

def equa_histo(image):
    histo_cumu1 = histo_cumu(image)
    histo_cumu_normalized = histo_cumu1 * 255 / histo_cumu1[-1]
    LUT = histo_cumu_normalized.astype(np.uint8)

    return LUT[image]


def equlisation_exact(image):
    
    im_ligne = image.reshape(-1) #met l'image en vecteur ligne
    
    im_ligne_sorted = np.argsort(im_ligne) 
    
    uniform_value = np.linspace(0,255,im_ligne_sorted.shape[0])
    im_ligne[im_ligne_sorted] = uniform_value
    equalized_image = im_ligne.reshape(image.shape).astype(int)
    return equalized_image
    
def seuil(image):
    