''' This is a simple Python script for playing a game of MASH game-
#Mansion, Apartment, Shack, House'''
print("Welcome to MASH  Mansion, Apartment, Shack, House. Press ENTER after every question")
import random
fixa = int(input("Choose a number between 1 and 3 "))
if fixa == 1:
    a = 'Mansion'
elif fixa == 2:
    a = 'Apartment'
elif fixa == 3:
    a = 'Shack'
else:
    a = 'Nothing!'


    print ("Good Choice")

print("Names of 3 people of the opposite gender")
d=input("> ")
e=input("> ")
f=input("> ")
print("Good Choice")

print("Choose any 3 jobs you would like to do")
g=input("> ")
h=input("> ")
i=input("> ")

print("Good Choice")
variable_list2 = [d,e,f]
variable_list3 = [g,h,i]
random_variable2 = random.choice(variable_list2)
random_variable3 = random.choice(variable_list3)
print ("You will live in a " + a)
print ("You will marry " +   random_variable2)
print ("You will become a " + random_variable3)
Reuben = input =("Did you enjoy the game")
if Reuben == "Yes":
    print("Thankyou for Playing!")
