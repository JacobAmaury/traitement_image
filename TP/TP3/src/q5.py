import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

def run_q5(): 
    print("5. Focus on the center of interest of an image without distorting the overall image or context too much.")
    eiffel = func.open_image("../Images_TP/tour-eiffel.jpg", "RGB")
    mask = func.focus_center(eiffel,210, 30)
    plt.subplot(1,2,1)
    plt.imshow(eiffel)
    plt.subplot(1,2,2)
    plt.imshow(mask)
    plt.show()