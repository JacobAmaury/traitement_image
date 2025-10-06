import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

path_flag = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/France.png"
path_mark = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Mark.png"
france_flag = open_image(path_flag)
image_mark = open_image(path_mark)

def run_q4():
    print("Question 4: Mix of a photo and a flag")
    print("I had many problems of type for this question.")
    im = picture_flag(image_mark, france_flag)
    
    plt.imshow(im)
    plt.show()
    