import func
import matplotlib.pyplot as plt
import os 
import sys
import time
import image_1
import image_2
import image_3



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress enter to get back to the menu")

def menu():
    while True:
        clear_screen()
        print("===============================")
        print("Global Minimum for Active Contour Models: A Minimal Path Approach")
        print("===============================")
        print("1. Image 1 working")
        print("2. Image 2 working")
        print("3. Image 3 working")
        print("4. Exit")
        print("===============================")
        choice = 0
        choice = input("Choose one of the topics: ").strip()
        
        if choice == "1":
            clear_screen()
            image_1.run_image_1()
            pause()
        elif choice == "2":
            clear_screen()
            image_2.run_image_2()
            pause()
        elif choice == "3":
            clear_screen()
            image_3.run_image_3()
            pause()
        elif choice == "4":
            break    


menu()


