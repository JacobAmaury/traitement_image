import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

def run_q3(): 
    print("3. Context-Aware Image Resizing")
    print("This is quite long to execute — you can reduce the iteration number.")
    print("This code took me some time to understand, but it works really well.")

    resize = func.open_image("../Images_TP/Resize.png", "RGB")
    resized = resize.copy()
    itt_num = 100
    for i in range(itt_num):
        resized = func.seam_carving(resized)
        print(f'seamcarving applied {i}')
    plt.subplot(1,2,1)
    plt.imshow(resize)
    plt.subplot(1,2,2)
    plt.imshow(resized)
    plt.show()
