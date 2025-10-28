import func
import matplotlib.pyplot as plt
import numpy as np

import os 
import sys
import time
import Q1
import Q2
import Q3
# import q4
# import q5



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress enter to get back to the menu")

def menu():
    while True:
        clear_screen()
        print("===============================")
        print("TP3")
        print("Question 5 and 6 are in src/question6 or 7")
        print("===============================")
        print("1. Le photomaton.")
        print("2. All RGB")
        print("3. Mesures")
        print("4. Exit")
        print("===============================")
        choice = 0
        choice = input("Choose one of the topics: ").strip()
        
        if choice == "1":
            clear_screen()
            Q1.run_q1()
            pause()
        elif choice == "2":
            clear_screen()
            Q2.run_q2()
            pause()
        elif choice == "3":
            clear_screen()
            Q3.run_q3()
            pause()
        elif choice == "4":
            break    


menu()


