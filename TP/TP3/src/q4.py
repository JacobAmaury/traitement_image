import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

def run_q4(): 
    print("4. Interactive Depth of Field.")
    print("For this question, I have manually defined the depth map.")

    img = func.open_image("../Images_TP/Profondeur.png")
    result = func.focus_two_zones(img,
                             zone1_center=0.70, zone1_width=0.50, z1_top=0.0, z1_bottom=1,
                             zone2_center=0.40, zone2_width=0.15, z2_top=0.3, z2_bottom=1)

    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title("Image originale")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Effet de profondeur de champ")
    plt.imshow(result)
    plt.axis('off')
    plt.show()
