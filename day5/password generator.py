
import random
all_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

all_symbols = ['!','@','#','%','&','(',')', '-','+','=','<','>','{',"}",'[', ']','/']
all_numbers = ['0','1','2','3','4','5','6','7','8','9']

    
alphabets = int(input("How many alphabet's you want in your password ?\n"))
symbols = int(input("How many symbol's you want in your password ?\n"))
numbers = int(input("How many number's's you want in your password ?\n"))
password_list = []
for char in range(1, alphabets+1 ):
   password_list.append (random.choice(all_alphabets)) 

for char in range(1, symbols+1 ):
   password_list.append(random.choice(all_symbols) )


for char in range(1, numbers+1 ):
   password_list.append(random.choice(all_numbers))

random.shuffle(password_list)


password = ""
for char in password_list:
   password += char 

print(password)