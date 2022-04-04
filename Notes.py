#Modules 1) import csv, 2) import random, 3) import numpy 




# Set Variable for list
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

# Get first item in the "counties" list
counties[0]

# Use print statement
print(counties[2])

# Negative Index's - identify last position relative to end of list
print(counties[-1])
# To get to the second last item, type -2
print(counties[-2])

# Find length of a list
len(counties)

# Find certain items from list (Arapahoe & Denver)
counties[0:2]

# Get first and second items from list
counties[:2]

# Add items to a list
counties.append("El Paso")

# Specify where to add new item to a list
counties.insert(2, "El Paso")

# Remove an item from a list
counties.remove("El Paso")

# Remove an item from a specific index number
counties.pop(3)
'El Paso'

# Exchange Jefferson county (2) with El Paso
counties[2] = "El Paso"





# Tuples cannot have items added or removed from them
counties_tuple = ("Arapahoe","Denver","Jefferson")

# Index and slice to get value (Denver)
counties_tuple[1]







# Create empty Dictionary
counties_dict = {}

# Add Arapahoe to dictionary as key and number of registered voters as value
counties_dict["Arapahoe"] = 422829

# Repeat two more times to add more to dictionary
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

# Get length of dictionary
len(counties_dict)

# Get all keys and values - gives you the view object - cannot use list indexing with .items
counties_dict.items()

# Get all the keys
counties_dict.keys()

# Get all the values
counties_dict.values()

# Get specific value
counties_dict.get("Denver")



# Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get only the keys (county name) from dictionary
for county in counties_dict:
    print(county)
# You can also do this with 'keys' method
for county in counties_dict.keys():
    print(county)

# Get values of a dictionary
for voters in counties_dict.values():
    print(voters)













# If Else Practice
counties = ["Arapahoe","Denver","Jefferson"]

# == is comparison operator equal to
if counties[1] == 'Denver':
    print(counties[1])


# Membership operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# Logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")









# If Else Practice
#What is the score?
from ast import Or


score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


#Or - Example 2
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')



# If Else Practice
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")



# While Loop
# Set Variable
x = 0
# Test if x is less than or equal to 5
while x <= 5:
# If TRUE, print x
    print(x)
# Increment x by 1 until condition is false
    x = x + 1














# Iterate through lists and tuples
for county in counties:
    print(county)

# Built in range function example
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
# simplify this code by:
for num in range(5):
    print(num)

# Iterate through counties using rang
# i indicates the index
# Answers how many counties in list
for i in range(len(counties)):
    print(counties[i])


# Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get only the keys (county name) from dictionary
for county in counties_dict:
    print(county)
# You can also do this with 'keys' method
for county in counties_dict.keys():
    print(county)

# Get values of a dictionary
for voters in counties_dict.values():
    print(voters)
#ALSO
for county in counties_dict:
    print(counties_dict.get(county))

# Get Key-Value pairs of dictionary
for key, value in dictionary_name.items():
    print(key, value)
    #OR - county and voters swapped for key and value
for county, voters in counties_dict.items():
    print(county, voters)




# Import csv
import csv
    # Look at functions in csv import tools
dir(csv)


# Only list functions with String types
dir(str)





# Direct path to file
# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


# Inderect path to file
import os
# Directory of os
dir(os)
# We need 'os.path'
dir(os.path)
# We need join()
