
alphabets =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text,shift_amount,cipher_direction):
  end_text =""
  if cipher_direction == "decode":
      shift_amount *= -1
  for char in start_text:
    if char in alphabets:
     position = alphabets.index(char)
     new_position = position + shift_amount   
     end_text += alphabets[new_position]
    else:
     end_text += char

  print(f"The {cipher_direction} text is {end_text}")  

run_again = True
while run_again:
  direction = input("1.Type encode to Encrypt message\n2.Type decode to Decrypt message\n")
  message = input("Type your message\n")
  shift = int(input ("type shift numbers\n"))
  shift = shift % 26
  ceaser(start_text=message,cipher_direction=direction,shift_amount=shift)
  result = input("type 'yes' you want to encode or decode again . or type  no\n")
  if result == "no":
    run_again = False
    print("Goodbye :)")