print("Welcome to pizza hut")
size = input("What size pizza do you want? S / M / L\n")
pepperoni = input("Do you want to add pepperoni ? Y / N\n")
cheese =  input("Do you want extra cheese? Y / N\n")
bill = 0
size.lower()
pepperoni.lower()
cheese.lower() 

if size == "s" :
    bill =  15

elif size == "m" :
    bill = 20

elif size == "l":
    bill = 25 
    
    

if pepperoni == "y":
    if size == "s":
      bill += 2
    
    else :
        bill += 3

if cheese == "y" :
    bill += 1         


print(f"\nTotal bill $ {bill}")


