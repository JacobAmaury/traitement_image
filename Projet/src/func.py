import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
from scipy.ndimage import laplace
import cv2 as cv

def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img

def pretreatment(image):
    """In this function we normalize and denoise the image"""
    image = image/np.max(image)
    image = cv.GaussianBlur(image,(3,3),0)
    return image

def p_tild(image ,mode=0, alpha=50, sigma=1.0, omega=0.05):
    """This function compute p_tild. if mode = 0 P = exp(-alpha * g^2) else P = 1 / (1 + (g/sigma)^2)"""
    Gy, Gx = np.gradient(image)
    g = np.sqrt(Gx**2 + Gy**2)

    p = np.empty_like(image)
    if mode == 0 :
        p = np.exp(-alpha*(g**2))
    else:
        p = 1/(1+(g/sigma)**2)
    p_tild = omega + p

    return p_tild
    
