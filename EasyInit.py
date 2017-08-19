import argparse
import random

# Check if a list was specified
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file",
    help="A comma-separated file containing characters to automatically roll for and their initiative bonuses")
args = parser.parse_args()

# Initialising the initiatives array
initiatives = []

# If a file was specified, open it.
if (args.file):
    with open(args.file, newline='') as init_file:
        for line in init_file:
            # Split the line into the character name and initiative bonus
            line_info = line.split(",")
            name = line_info[0]
            init = random.randint(1, 21) + int(line_info[1])
            initiatives.append((name, init))

# If not, prompt the user to input the values
else:
    # Request a name and predetermined initiative roll until a blank name is entered
    while (True):
        name = input("Enter a character name, or press enter to move on: ")
        if (name == ""):
            break
        init = int(input("Enter this character's initiative roll: "))
        initiatives.append((name, init))

# Setting up the generic enemies, using the same system as above
while (True):
    name = input("Enter a generic enemy name, or press enter to move on: ")
    if (name == ""):
        break
    # Get an initiative bonus for enemies
    enemy_bonus = int(input("Enter the enemies' initiative bonus: "))
    qty = int(input("How many of these enemies to create: "))
    for i in range(qty):
        curr_name = name + " " + str(i+1)
        curr_init = random.randint(1, 21) + enemy_bonus
        initiatives.append((curr_name, curr_init))

# Sort the list
initiatives.sort(key=lambda tup: tup[1], reverse=True)

# Pretty-print the list
for pair in initiatives:
    print(str(pair[0]) + "\t" + str(pair[1]))

