year = int(input("Enter the year\n"))


if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")    
    else:  
       print ("leap year")    
else:
    print("Not a leap year. ")        