#/*
# * Auteur : Jacob Amaury                 |\      _,,,---,,_
# * Date   : 03102025 08:49:38     ZZZzz  /,`.-'`'    -.  ;-;;,_
# *                                      |,4-  ) )-,_. ,\ (  `'-' 
# */                                    '---''(_/--'  `-'\_)


# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# from function import *
import os 
import sys
import time
import q1

# path_flag = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/France.png"
# path_mark = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/Mark.png"
# path_text_rest = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/texte_a_restaurer.png"
# path_photo_rest = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/photo_a_restaurer.png"

# image_photo_rest = open_image(path_photo_rest, "L")
# im_text_rest = open_image(path_text_rest, "L")
# france_flag = open_image(path_flag)
# image_mark = open_image(path_mark)
# image_clown = open_image(path_clown,"L")
# image_noisy_Lena = open_image(path_noisy_lena)
# image_Lena = open_image(path_lena)
# image_noise = open_image(path_noise, "L")

#filtered_clown(image_clown)
#filtered_noise(image_noise)


# Lena_de_noise = median(image_noisy_Lena, 4)
# Lena_de_noise_equa = equlisation_exact(Lena_de_noise)
# histo_Lena,bin_lena = np.histogram(Lena_de_noise_equa, 255)

# plt.subplot(1,2,1)
# plt.bar(bin_lena[:-1],histo_Lena)
# plt.subplot(1,2,2)
# plt.imshow(Lena_de_noise_equa)



# Mark_france = picture_flag(image_mark, france_flag)

# plt.imshow(Mark_france)
# image_photo_rest



# plt.subplot(1,2,1)
# plt.imshow(image_photo_rest, cmap="gray")
# plt.subplot(1,2,2)
# plt.imshow(im_text_rest_equa , cmap="gray")
# plt.show()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress enter to get back to the menu")

def menu():
    while True:
        clear_screen()
        print("===============================")
        print("TP3")
        print("===============================")
        print("1. Median filter")
        print("2. Periodic noise filtering")
        print("3. Supresion of noise")
        print("4. Mix of a photo and a flag")
        print("5. Histogramme equalisation")
        print("6. Restauration of printed document")
        print("7. Quit")
        print("===============================")
        choice = 0
        choice = input("Choose one of the topics: ").strip()
        
        if choice == "1":
            clear_screen()
            q1.run_q1()
            pause()
        elif choice == "0":
            print("tptp")
        else:
            print("tata")    


menu()