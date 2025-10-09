import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from function import *

path_flag = "../Images_TP/France.png"
path_mark = "../Images_TP/Mark.png"
france_flag = open_image(path_flag)
image_mark = open_image(path_mark)

def run_q4():
    print("Question 4: Mix of a photo and a flag")
    print("I had many problems of type for this question.")
    print("Do not forget to close the matplotlib window in order to go back to the menu")
    im = picture_flag(image_mark, france_flag)
    
    plt.imshow(im)
    plt.show()
    