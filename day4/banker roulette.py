import random
names_input = input("Give me everybodys name seperated by a comma. ")
#using split string method to remove space and commas
names = names_input.split(", ")
index_of_list = len(names)

number = random.randint(0 ,index_of_list - 1)

print(names[number] + " will pay the bill")

