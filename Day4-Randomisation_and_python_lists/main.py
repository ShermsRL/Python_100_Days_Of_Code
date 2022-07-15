# Day 4 Lesson---------------------------------------------------------------------------------------------------------
# import random #modules is a piece of code focused on one function so that code is not too cluttered
# import My_module

# random_integer = random.randint(1, 10) #generate a number from 1 to 10
# print (random_integer)

# random_float = random.random() * 5 #generate a random float number between 0.0 to 1.0
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# print(My_module.pi)

# states_of_america = ["Deleware", "Pennsylvania"]

# print(states_of_america[0])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])


# Day 4 Challenge------------------------------------------------------------------------------------------------------
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = [rock, paper, scissors]
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >= 3 or user_choice < 0:
  print("You dumb dumb, you lose")
else:
  print(rps[user_choice])
  print("Computer Choose \n")

  computer_choice = random.randint(0, 2)
  print(rps[computer_choice])

  if user_choice >= 3 or user_choice < 0:
    print("You dumb dumb, you lose")
  elif computer_choice == user_choice:
    print("Its a draw")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice == 1 and user_choice == 0:
    print("You lose")
  elif computer_choice == 2 and user_choice == 1:
    print("You lose")
  else:
    print("You win")


