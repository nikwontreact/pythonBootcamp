print("Welcome to roller coaster ride")
height = int(input(" what is  your height in cm ?\n"))
bill = 0
if height >=120:
    print("\nYou can ride roller coaster!! ")
    age = int(input("What is your age ?\n"))
    
    if age < 12 :
        print("\nChild tickets are $5. ")
        bill = 5
    elif age <= 18 :
        print("\nYouth tickets are $7. ")
        bill = 7
    else :
        print("\nAdult tickets are $12. ")
        bill = 12
    wants_photo = input("\nDo you want photo for $3 ? Y / N \n")     
    
    if wants_photo == "y" :   
        bill += 3 
        print(f"\nplease  pay  ${bill}")
    else :     
         print(f"\nplease  pay  ${bill}")
else :
    print("\nsorry, you have to grow taller before you ride ")




