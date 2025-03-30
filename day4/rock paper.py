import random 
print("Welcome to rock paper scissor game ")

choice = input(" Type - 'ROCK' , 'PAPER' or SCISSOR  \n").lower()

if choice == 'rock':
  print(''' 

        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

  ''')
elif choice == 'paper':

  print('''

        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---._________)

  ''')

elif choice =="scissor":

  print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)


  ''')

else :
    exit()  

options = ['rock' , 'paper' , 'scissor']

random_choice = random.choice(options)

print("\nComputer choosed  " +random_choice)

if random_choice == 'rock':
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)


    ''')


elif random_choice == 'paper':
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---._________)

    ''')    

else :
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)

    ''') 




if choice == 'rock' and random_choice == 'paper':
    print("You lost") 

elif choice == 'paper' and random_choice == 'rock':
    print("You won") 

elif choice == 'rock' and random_choice == 'scissor':
    print("You won") 

elif choice == 'scissor' and random_choice == 'rock':
    print("You won") 



elif choice == 'paper' and random_choice == 'scissor':
    print("You lost") 

elif choice == 'scissor' and random_choice == 'paper':
    print("You won")

else :
    print("no one won")     
