print("WELCOME TO LIFE LEFT PROGRAM")
age = int(input("Enter your age "))

years_left = 90 - age

months_left = years_left * 12

weeks_left = round(months_left *4.345)

days_left = weeks_left * 7

if months_left > 0  and days_left  > 0  and days_left > 0 :

  print(f"you have {years_left} years , {months_left} months ,{weeks_left} {days_left} more to live" )

else:
    print("you have already lived enough , you should have died till now , die bitch ya time is up ")  