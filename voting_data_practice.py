# Create empty list
voting_data = []

# Add or append to each dictionary
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# Calculate percentage of votes a candidate recieves
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


# Get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


# Get the list of values from a dictionary
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Only print county name
for county_dict in voting_data:
    print(county_dict['county'])



# F-Strings

#Example
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#And here's how you would edit the code to use f-strings.
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")



# Skill Drill - Print each county and registered voter form the 
# counties dictionary so that the output looks like this:
    #Arapahoe county has 422829 registered voters.
    #Denver county has 463353 registered voters.
    #Jefferson county has 432438 registred voters.
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)




# add a thousands separator to the output for the candidate votes and total votes 
# and then format the percentage of votes to two decimal places. The code should look like this:
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

