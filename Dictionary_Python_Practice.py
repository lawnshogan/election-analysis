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