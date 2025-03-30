print("Welcome to BMI calculator")
height = float(input("Enter height in cm : \n"))
weight = float(input("Enter weight in kg : \n"))


bmi = round (weight / (height / 100)** 2)

print(f"your bmi is {bmi} ")

if bmi < 18.4:
    print("you are under weight")

elif  bmi < 24.9 :
    print("you have normal weight") 

elif  bmi < 29.9 :
    print("you are overweight")

elif  bmi < 34.9 :
    print("you are obese")

elif bmi > 39.9  :
    print("you are clinically obese")