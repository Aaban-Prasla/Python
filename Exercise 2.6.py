import random

# For the 3 digit passcode
One = random.randint(0,9)
Two = random.randint(0,9)
Three = random.randint(0,9)

# For the 4 digit passcode
Four = random.randint(0,9)
Five = random.randint(0,9)
Six = random.randint(0,9)
Seven = random.randint(0,9)

# For the 3 digit passcode
str_one = str(One)
str_two = str(Two)
str_three = str(Three)

# For the 4 digit passcode
str_four = str(Four)
str_five = str(Five)
str_six = str(Six)
str_seven = str(Seven)

print("3 digit passcode " + str_one + str_two + str_three)
print("4 digit passcode " + str_four + str_five + str_six + str_seven)
