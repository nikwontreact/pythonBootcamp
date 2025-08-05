#if number divisible by 3 print fizz if number divisible by 5 print fizz  if number divisible by 3 & 5 print fizzbuzz

print("welcome to fizz and buzz")
for number in range(1,200):
    if number %3 == 0 and number %5 == 0:
        print("fizz buzz")
    elif number %3 ==0 :
        print("fizz")
    elif number %5 == 0:
        print("buzz")
    else:
        print(number)