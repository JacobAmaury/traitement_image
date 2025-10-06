#/*
# * Auteur : Jacob Amaury                 |\      _,,,---,,_
# * Date   : 03102025 08:49:38     ZZZzz  /,`.-'`'    -.  ;-;;,_
# *                                      |,4-  ) )-,_. ,\ (  `'-' 
# */                                    '---''(_/--'  `-'\_)
import os 
import sys
import time
import q1
import q2
import q3
import q4
import q5
import q6
# path_photo_rest = "/home/amaury/Desktop/Cours/M1/S1/intro_Traitement_image/TP/TP2/Images_TP/photo_a_restaurer.png"

# image_photo_rest = open_image(path_photo_rest, "L")

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
        elif choice == "2":
            clear_screen()
            q2.run_q2()
            pause()
        elif choice == "3":
            clear_screen()
            q3.run_q3()
            pause()
        elif choice == "4":
            clear_screen()
            q4.run_q4()
            pause()
        elif choice == "5":
            clear_screen()
            q5.run_q5()
            pause()
        elif choice == "6":
            clear_screen()
            q6.run_q6()
            pause()
        elif choice == "7":
            break    


menu()