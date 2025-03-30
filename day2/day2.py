#getting height and weight
print ("Welcome to BMI calculator") 
height = input("Enter the height in meters ")
weight = input("Enter the weight in kilos ")

#converting string into int 
weight = int(weight)
height = float(height)

#calculating BMI
bmi = weight / height** 2
bmi = int(bmi)
print("Your Bmi is  ",bmi)