import random
# Initialising the initiatives array
initiatives = []
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
    qty = int(input("How many of these enemies to create: "))
    for i in range(qty):
        curr_name = name + " " + str(i+1)
        curr_init = random.randint(1, 21)
        initiatives.append((curr_name, curr_init))

# Sort the list
initiatives.sort(key=lambda tup: tup[1], reverse=True)

# Pretty-print the list
for pair in initiatives:
    print(str(pair[0]) + "\t" + str(pair[1]))