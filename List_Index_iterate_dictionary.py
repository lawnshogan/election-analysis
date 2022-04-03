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

