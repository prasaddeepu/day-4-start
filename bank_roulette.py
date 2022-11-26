import random
names_string = input("Give me everbody's name, sepereated with a comma. ")
names = names_string.split(", ")
print(names)
random_num = random.randint(0,len(names) - 1)
person = random.choice(names)

print(f"The person picked to pay the bill is: {person}" )
#new comment