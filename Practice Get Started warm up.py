# Get
# Get started Jypiter Noteook
# https://youtu.be/suAkMeWJ1yE?si=k_SYbyLXwJ6B149Z
# plus DAtaWrangle extensuon for data analyasis and visualization
-----------------

# comments write here and this way with Python 3.11.4, MS VS Code, Jupyter Notebook
#  source 1 get started 
#       - https://learn.microsoft.com/en-us/shows/intro-to-python-development/
# source 2 import csv file documentation
#       - https://docs.python.org/3/library/csv.html
# Purpose: to recall/ to warm up before real coding in Python
# Tools: Python 3.11.4, MS VS Code, Jupyter Notebook

#string concatenation
from datetime import datetime
import json


Fname = "Christopher"
Lname = "Nolan"
print('Hello, ' + Fname.upper() + ' ' + Lname.lower())

#number addition and power
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
print("The sum of {0} and {1} is {2}".format(first_number, second_number, int(first_number) + int(second_number)))
print("The power of {0} and {1} is {2}".format(first_number, second_number, float(first_number) ** float(second_number)))

#date and time functions    

import datetime
current_date = datetime.date.today()
print("Today's date is: " + str(current_date))

#conditional statements
input_price = input("Enter the price: ")
price = float(input_price)
if price >= 1.00:
    tax = 0.07
    print("The price is greater than or equal to 100. and Tax is " + str(tax))
else:
    tax = 0
    print("The price is less than 100. and Tax is " + str(tax))

#Collections - video 25 of 44
#list
names = ["Alice", "Bob", "Charlie"]
scores = []

scores.append(85) #Add new score to the list
scores.append(90)
print(names[0] + "'s score is: " + str(scores[0]))

#array
import array as arr
numbers = arr.array('i', [1, 2, 3, 4, 5])
numbers.append(6) #Add new number to the array
print("Array: The numbers in the array are: " + str(numbers))
print("Retrieve range: " + str(numbers[1:4])) #Retrieve range of numbers from index 1 to   3

#dictionary
student = {"name": "Alice", "age": 20, "grade": 85}
print("Dictionary: Student's name is: " + student["name"])

# looping - video #27
# for loop - 
#   for i in range(5):
#    print("looping: the value of i is: " + str(i)) 
# while loop - 
#   count = 0

#Functions - video #28
#Module - video #33
#Calling APIs -  [38 of 44] JavaScript Object Notation (JSON)

# Nest dictionaries to create JSON in format 
# {"Key1": {"SubKey0": "SubValue0", "Key3": "Value3",...} 
person_dict = {'FirstName': 'John', 'LastName': 'Doe'}
staff_dict = {}
staff_dict['Program Manager'] = person_dict
#convert dictionary to JSON Object
staff_json = json.dumps(staff_dict)
print("JSON Object: " + staff_json)

#Create a list of dictionaries to create JSON in format
languages_list = [
    {"Name": "Python", "Version": "3.8"},
    {"Name": "JavaScript", "Version": "ES6"}
]
#addlist to dictionary
person_dict ['languages'] = languages_list

#Convert dictionary to JSON Object
person_json = json.dumps(person_dict)
print(person_json);


#Using dotenv - Mamanaging Keys - Video 40 of 44
# for local environment variables
#Store enviromental variables in text file
#e.g. DATABASE Sample connection_String
#....

#Decorators - Video 42 of 44
#When you create own framework, you can use decorators to add functionality to your functions or classes without modifying their code. Decorators are a powerful feature in Python that allow you to wrap a function or class with another function, which can modify its behavior.
