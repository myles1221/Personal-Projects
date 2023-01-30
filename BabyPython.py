 
variable_loop = 0

import xdrlib



print("Welcome to Baby Python")

count= ""
number = 0 
k=0



number = input("How many triangles do you want to print?\nEnter:")

num_character = str(number)
print("\nYou want to print "+ num_character + " Trangles")

def num_triangle():
    k=0
    while(k<number):
        print("   /|")
        print("  / |")
        print(" /  |")
        print("/___|")
        k+=1

    print(num_character+" Trianlges printed.")





num_triangle()
