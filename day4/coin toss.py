import random

print("welcome to toss a coin program")
choice = input("Type 'yes' to toss a coin ").lower()
if choice == 'yes' or 'y' :
    random_side = random.randint(0,1)
    if random_side == 0 :
        print("HEADS")

    else :
        print("TAILS")
    
else :
    exit()

