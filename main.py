import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice= int(input("What do you choese? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

compute_choice= random.randint(0,2)

if choice == 0:
  if compute_choice == 0:
    print(f"{rock} \n Computer Chose: \n\n {rock} \n Draw!")
  elif compute_choice == 1:  
    print(f"{rock} \n Computer Chose: \n\n {paper} \n You Lost!")
  else:
    print(f"{rock} \n Computer Chose: \n\n {scissors} \n You Won!")
elif choice == 1:   
  if compute_choice == 0:
    print(f"{paper} \n Computer Chose: \n\n {rock} \n You Won!")
  elif compute_choice == 1:  
    print(f"{paper} \n Computer Chose: \n\n {paper} \n Draw!")
  else:
    print(f"{paper} \n Computer Chose: \n\n {scissors} \n You Lost!")
elif choice == 2:
  if compute_choice == 0:
    print(f"{scissors} \n Computer Chose: \n\n {rock} \n You Lost!")
  elif compute_choice == 1:  
    print(f"{scissors} \n Computer Chose: \n\n {paper} \n You Won!")
  else:
    print(f"{scissors} \n Computer Chose: \n\n {scissors} \n Draw!")
else:
  print("Your choice is unvalid!")