print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************  
''')

print("Welcome to the Treasure Island.")
print("Finding the treasure will save you from impending doom")
op1 = input("First, let's pick a path, left or right? ")
if(op1.lower() == "left"):
    print("You found a snake, game over.")
elif(op1.lower() == "right"):
    op1_2 = input("You continue through the trees and find more choices, to the left it appears to be an abbandoned cottage, to the right is the coast, left or right? ")
    if(op1_2.lower() == "left"):
        op1_2_1 = input("You get to the cottage and find a pistol. Do yo want to take it? Y or N ")
        if(op1_2_1.lower() == "y"):
            print("You exit the cottage and encounter a mutant rabbit, luckily you have your trusty pistol in hand, right?, no, the pistol was empty, game over.")
        elif(op1_2_1.lower() == "n"):
            print("You exit the cottage and encounter a mutant rabbit, you left the pistol in the cottage, game over.")
    elif(op1_2.lower() == "right"):
        op1_2_2 = input("You get to the coast and find a boat, do you want to get on it? Y or N ")
        if(op1_2_2.lower() == "y"):
            print("Yo get to the other side of the island and find the treasure, congratulations!")
        elif(op1_2_2.lower() == "n"):
            print("While deciding you get ambushed by ann unknown animal. game over.")