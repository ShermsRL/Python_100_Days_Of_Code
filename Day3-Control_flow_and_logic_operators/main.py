# Day 3 Lesson
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Midlife tickets are 0")
    else:
        bill = 12
        print("Adult tickets are 12")

    wants_photo = input("Do you want a photo taken? Y or N?")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")

# Day 3 Project --------------------------------------------------------------------------------------------
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

cod = input("You arrived at the crossroad, would you like to go left or right? ")
cod_lower = cod.lower()
if cod_lower != "left":
    print("You fall into a hole and die")
else:
    print("You survive")
    sea = input("You arrive at the sea, would you like to swim or wait?")
    sea_lower = sea.lower()
    if sea_lower != "wait":
        print("Attacked by cheng hao, you die")
    else:
        print("You survive")
        door = input("You arrived in front 3 doors, pick red, yellow or blue.")
        door_lower = door.lower()
        if door_lower == "red":
            print("Burn by fire, you die.")
        elif door_lower == "blue":
            print("Eaten by beast, you die.")
        elif door_lower == "yellow":
            print("You Win!")
        else:
            print("Game over")
