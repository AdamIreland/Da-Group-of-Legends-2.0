from time import sleep
import random

def random1():
  print("this is a random piece of food from your fridge: ")
  rand=random.choice(list1)
  print(rand)

def ham():
  print("calories=150")
  
def milk():
  print("If you have 3 litres, then calories = 3000. ")
  print("If you have 2 litres, then calories = 2300. ")

def egg():
  print("1 Egg is 155 calories. A dozen eggs is 936 calories. ")

def banana():
  print("A banana is 89 calories.")
  


list1=[]
objects=["gun", "table", "chair"]

while True:
  user=input("Name one thing in your fridge: ")
  user=user.lower()
  list1.append(user)
  
  if user in objects:
    print("This does not belong in a fridge. ")
    list1.remove(user)
  if user == "nothing":
    list1.remove("nothing")
    print(list1)
    break
  print(list1)


ham()
