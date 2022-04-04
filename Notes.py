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