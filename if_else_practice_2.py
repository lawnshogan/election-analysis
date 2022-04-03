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





















#OTHER PRACTICE



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










#OTHER EXAMPLES


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