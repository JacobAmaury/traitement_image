import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

def run_q1(): 
    
    
    print("1. Re-focusing of an image from a sequence.")
    print("To do this question I have calculed the contrast of the 3 images and we took the highest contrast.")
    print("As we can see the result is not perfect.")
    
    path_images = ["../Images_TP/Refocus_1.png", "../Images_TP/Refocus_2.png", "../Images_TP/Refocus_3.png"]
    refocus = func.refocus(path_images)
    plt.title("image refocus")
    plt.imshow(refocus)
    plt.show()

