print("WELCOME TO TIP CALCULATOR")
bill = float(input(" What was the total bill $ \n"))   

tip = int(input("How much tip would you like to give ? 10, 12, or 15 ? \n"))

people = int(input("How many people to split the bill ?\n"))

#calculating total bill with tip
bill_with_tip = tip / 100 * bill + bill
print(f"total bill with tip {bill_with_tip}")

bill_per_person =  bill_with_tip / people 
round(bill_per_person,2)

print(f"Each person should pay ${bill_per_person} ")

