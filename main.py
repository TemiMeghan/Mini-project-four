# ****************************************************************
# mini project 4
# learning python basics continuation
# programs on conditions, if, elif and else, rock, paper, scissors game with the computer and I and use of random package
# ****************************************************************
import random  #imports random package
#Task 1
print("Task 1")
print()  # indicates a space
# A program that prints a series of 7 conditional tests
# Condition1: Testing for equality and inequality with strings
print("Condition 1")
city = "Sudbury"  # name of city
print("Is city == Sudbury? My prediction is True.")  # prints my prediction
print(city == "Sudbury")  # test if city equates Sudbury using ==
print("Is city != Sudbury? My prediction is False")  # prints my prediction
print(city != "Sudbury")  # test if city doesn't equates Sudbury using !=
print()  # indicates a space
# Condition 2: tests using the lower() method.
print("Condition 2")
print(
  "Is city.lower() == Sudbury? My prediction is False")  # prints my prediction
print(city.lower() == "Sudbury")  # test if city.lower() equates Sudbury
print()  # indicates a space
# Condition 3: numerical tests for equality and inequality
print("Condition 3")
chosen_number = 7  #Chosen number for the test
print("Is chosen_number == 7? My prediction is True.")  # prints my prediction
print(chosen_number == 7)  # tests if chosen_number equates 7 using ==
print("Is chosen_number != 7? My prediction is False")  # prints my prediction
print(
  chosen_number != 7)  # test if chosen_number doesn't equates Sudbury using !=
print()  # indicates a space
# Condition 4: tests greater than and less than, greater than or equal to, and less than and equal to
print("Condition 4")
print("Is chosen_number > 7? My prediction is False")  # prints my prediction
print(chosen_number > 7)  # tests if chosen_number is greater than 7
print("Is chosen_number < 7? My prediction is False")  # prints my prediction
print(chosen_number < 7)  # tests if chosen_number is less than 7
print("Is chosen_number >= 7? My prediction is True")  # prints my prediction
print(
  chosen_number >= 7)  # tests if chosen_number is greater than or equal to  7
print("Is chosen_number <= 7? My prediction is True")  # prints my prediction
print(chosen_number <= 7)  # tests if chosen_number is less than or equal to  7
print()  # indicates a space
# Condition 5: tests that use and / or keyword operators
print("Condition 5")
first_meal = "Pasta"  # a first meal variable that contains pasta
meal_pots = 5  # number of meal_pots available
if first_meal == "Pasta" and meal_pots >= 7:  # using AND operator to test if first_meal equates Pasta and meal_pots is >= 5
  print("My prediction is True")  # prints my prediction
  print("True")  # result prints if condition is true
else:
  print("My prediction is false")  # prints my prediction
  print("False")  # result prints if condition is false.
print()  # indicates a space
# Condition 6: test if the item is in a list
print("Condition 6")
items = ["Water", 5, "Fruits", 10]  # a list of items
if "Water" in items:  # checks if Water is in items list
  print("Is Water in items? My prediction is True")  # prints my prediction
  print("True")  # result
else:
  print("My prediction is False")  # prints my prediction
  print("False")  # result
print()  # indicates a space
# Condition 7: test if the item is not in a list
print("Condition 7")
if 70 in items:  # checks if value 70 is in items list
  print("Is 70 in items? My prediction is True")  # prints my prediction
  print("True")  # result
else:
  print("Is 70 in items? My prediction is False")  # prints my prediction
  print("False")  # result
print()  # indicates a space
# Task 2
print("Task 2")
# A program that plays a rock, paper, scissors game with the computer and I
games = ["Rock", "Paper", "Scissors", "Temitope"]  # a list of items in a game
my_pick = random.choice(games)  # my random choice
computer_pick = random.randint(1, 4)  # computer's random choice
if my_pick == "Rock":
  my_pick = 1  # assigning the value 1 to Rock
elif my_pick == "Paper":
  my_pick = 2  # assigning the value 2 to Paper
elif my_pick == "Scissors":
  my_pick = 3  # assigning the value 3 to Scissors
elif my_pick == "Temitope":
  my_pick = 4  # assigning the value 4 to my name
print("My pick is ", my_pick)  # My pick printed
print("Computer pick is ", computer_pick)  # Computer's pick printed
if my_pick == computer_pick:
  print("Oh, it's a tie, you win"
        )  # if my value and computer value are the same, computer wins
else:
  my_pick != computer_pick
  print("Sorry, you loose"
        )  # if my value and computer value are not the same, computer loose
print()  # indicates a space
# Task 3
print("Task 3")
# A program that calculates BMI based on weight ranges.
weight_kg = 75  # weight value
height_m2 = 1.45  # height value
BMI = weight_kg/(height_m2**2)  # BMI formula
if BMI >= 40.0:  # first condition
  print(f" Your BMI is {BMI} and it is classified under Obese class III and this has an extremely high chance of health issues") # result if condition is true.
elif BMI >= 35.0 and BMI >= 39.9:  # second condition
  print(f" Your BMI is {BMI} and it is classified under Obese class II and this has a very high chance of health issues") # result if condition is true.
elif BMI >= 30.0 and BMI >= 34.9:  # third condition
  print(f" Your BMI is {BMI} and it is classified under Obese class I and this has a high chance of health issues") # result if condition is true.
elif BMI >= 25.0 and BMI >= 29.9:  # fourth condition.
  print(f" Your BMI is {BMI} and it is classified under Overweight and this has an increased chance of health issues") # result if condition is true.
elif BMI >= 18.5 and BMI >= 24.9:  # fifth condition.
  print(f" Your BMI is {BMI} and it is classified under Normal Weight and this has a least chance of health issues") # result if condition is true.
elif BMI < 18.5:  # sixth condition.
  print(f" Your BMI is {BMI} and it is classified under Underweight and this has an increased chance of health issues") # result if condition is true.
else:  # seventh condition
  print(f"You really need to see a doctor, because your BMI is {BMI}") # result if condition is true.
print()  # indicates a space
# Task 4
print("Task 4")
# a program that selectes candidates and sends a message to them for a pizza program with an reward, not selected candidates are encouraged to join and obtain a reward
# pizza custormer list
premium_customers = ["Akin", "Paul", "Aayu", "Bilz", "Emmae"]
# pizza candidate list
premium_candidates = ["Femi", "Aayu", "Iffy", "Akin", "Oyin"]
for selected in premium_candidates:  # a loop that checks for selected candidates
  if selected in premium_customers:
    print(f"{selected} you've been selected as a member and have been rewarded a unique membership card that allows you to get the pizza of your choice for free")  # program for selected candidates
    print() # indicates a space
  else:
    print(f"Sorry, {selected} you're not selected as a member. You can participate, becoming a member helps you get a unique membership card that allows you to get the pizza of your choice for free")  # program for unselected candidates
    print() # indicates a space
print()  # indicates a space
# Task 5
print("Task 5")
print()  # indicates a space
# A program that prints the proper ordinal ending to the number (1st, 2nd, 3rd, 4th, etc), and print each result to a new line.
values = [1,2,3,4,5,6,7,8,9]  # values 1 to 9 in a list
for value in values:  #loops through the values list
  if value == 1:  # value equates 1
    print("This is the 1st number")  # first number printed
    print()   # indicates a space
  elif value == 2:  # value equates 2
    print("This is the 2nd number")  # second number printed
    print()   # indicates a space
  elif value == 3:  # value equates 3
    print("This is the 3rd number")  # third number printed
    print()   # indicates a space
  elif value == 4:  # value equates 4
    print("This is the 4th number")  # fourth number printed
    print()   # indicates a space
  elif value == 5:  # value equates 5
    print("This is the 5th number")  # fifth number printed
    print()   # indicates a space
  elif value == 6:  # value equates 6
    print("This is the 6th number")  # sixth number printed
    print()   # indicates a space
  elif value == 7:  # value equates 7
    print("This is the 7th number")  # seventh number printed
    print()   # indicates a space
  elif value == 8:  # value equates 8
    print("This is the 8th number")  # eighth number printed
    print()   # indicates a space
  elif value == 9:  # value equates 9
    print("This is the 9th number")  # nineth number printed
    print()  # indicates a space
# Task 6
print("Task 6")
print()  # indicates a space
# A program that allows the computer guess the value of a player
computer = random.randint(1,10)  # computer selects random number
player_value = 7  # player value
if computer == player_value: #checks if computer's value equates player's value
  print("Nice Guess! You got it")  #prints a message
  print(computer)  # prints the value computer chose
elif computer > player_value:  #checks if computer's value is greater than player's value
  print("Wrong Guess! The value is high")  #prints a message
  print(computer)  # prints the value computer chose
else:
  computer < player_value  #checks if computer's value is less than player's value
  print("Wrong Guess! The value is low")  #prints a message
  print(computer)  # prints the value computer chose
# Task 7
print("Task 7")
print()  # indicates a space
# A program that uses a random package to print two lists containing a total of three numbers after computer randomly rolls a six sided die
die = [random.randint(1,6)]  # first die  roll
print(die)  # roll output
die1 = [random.randint(1,6)]  # second die roll
die2 = [random.randint(1,6)]  # third die roll
die1.append(die2)  # appended two die rolls
dice = [die1] # appended result assigned to variable dice
print(dice)  # result of dice printed
print()  # indicates a space
# Task 8
print("Task 8")
print()  # indicates a space
# A program that prints the temperature of a city  in celsius, fahrenheit, and kelvin.
celsius_temp = 18  # temperature in celsius
fahrenheit_temp = (celsius_temp*(9/5)) + 32  # formula for fahrenheit
kelvin_temp = celsius_temp + 273.15  # formula for kelvin
# prints the temperature of the city where I was born
print(f"The weather in Lagos is {celsius_temp}C in Celsius which is {fahrenheit_temp}F in Fahrenheit and {kelvin_temp}K in Kelvin.")  
print()  # indicates a space
# Task 9
print("Task 9")
print()  # indicates a space
# an example and brief explanation of what I learnt from https://www.w3schools.com/python/
# a learning on Sets
print(""" 
          Sets are used to store multiple items in a single variable /n
          They are unordered, unchangeable, and unindexed which means they do not
          appear in an orderly manner and cannot be changed and you cannot access
          elements in a set by index. Also they are denoted by a {} curly brackets.
          An example is shown below:
      """)
fruits = {"apple", "oranges", "strawberry"}
print(fruits)  # prints in an unordered manner
# print(fruits[1])  # prints an error, this indicates you can't access an element by its index
print("strawberry" in fruits)  # prints true, you can use in to access elements in a set
# you can use the add() to add elements into a set
fruits.add("pawpaw")
print(fruits)
print()  # indicates a space
# Task 10
print("Task 10")
print()  # indicates a space
# A program that prints out a random card using an fstring and the random package.
card_numbers = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]  # list of card numbers
suits = ["clubs", "diamonds", "spades", "hearts"]  # list of suits

randomcard_numbers = random.choice(card_numbers)  # random card numbers chosen
random_suit = random.choice(suits)  # random suits chosen
# computer result after random pick
print(f"You've got the {randomcard_numbers} of {random_suit} ")




