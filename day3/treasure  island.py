print("WELCOME TO TREASURE ISLAND GAME")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

''')
print("you mission is to find treasure")
choice1 = input('You\'re at crossroads where you wanna go ? "left" / "right" \n').lower()

if choice1 == 'left':
  choice2 = input('you\'hv come to lake . There is an island in the middle of the lake . Type "wait" to wait for a boat . type "swim" to swim across.\n').lower()
    
  if choice2 == 'wait':
    choice3 = input("You arrived island unharmed. There is a house with 3 doors . one red, one yellow, one blue . Which color do you choose ? \n").lower()
    
    if choice3 == "red":
       print("Room full of fire . GAME OVER")
    elif choice3 == 'yellow':
       print("You found treasure you win!!!\n")
       print('''8b        d8 ,ad8888ba,   88        88    I8,        8        ,8I  ,ad8888ba,   888b      88  
 Y8,    ,8P d8"'    `"8b  88        88    `8b       d8b       d8' d8"'    `"8b  8888b     88  
  Y8,  ,8P d8'        `8b 88        88     "8,     ,8"8,     ,8" d8'        `8b 88 `8b    88  
   "8aa8"  88          88 88        88      Y8     8P Y8     8P  88          88 88  `8b   88  
    `88'   88          88 88        88      `8b   d8' `8b   d8'  88          88 88   `8b  88  
     88    Y8,        ,8P 88        88       `8a a8'   `8a a8'   Y8,        ,8P 88    `8b 88  
     88     Y8a.    .a8P  Y8a.    .a8P        `8a8'     `8a8'     Y8a.    .a8P  88     `8888  
     88      `"Y8888Y"'    `"Y8888Y"'          `8'       `8'       `"Y8888Y"'   88      `888  ''')
   
    elif choice3 == 'blue':
       print("You entered in a room of vampires . GAME OVER")
       
    else:
        print("you choked on water and died")    
  else:
     print("You got attacked by an trout")

else:
    print("You fell into a hole . GAME OVER")