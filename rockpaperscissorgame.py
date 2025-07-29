
import random


rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user=int(input("Enter 0 for rock, 1 for paper and 2 for scissor"))

if(user==0):
    print(rock)
elif(user==1):
    print(paper)
elif(user==2):
    print(scissor)

computer = random.randint(0,2)

if(computer==0):
    print(rock)
elif(computer==1):
    print(paper)
elif(computer==2):
    print(scissor)



if(user==computer):
    
    print("Draw")

elif(user==0 and computer==1):
    print("You lost")
elif(user==1 and computer==2):
    print("You lost")
elif(user==2 and computer==0):
    print("You lost")
else:
    print("You won")


