import random

print("rock paper and scissors ")
choose = int(input("what do you choose type 0 for rock,1 for paper or 2 for scissors:"))
if choose == 0:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    print(f"you chose:{rock}")
elif choose == 1:
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    print(f"you chose:{paper}")
elif choose == 2:
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    print(f"you chose:{scissors}")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papers = '''
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
game_images = [rock, papers, scissors]
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
if computer_choice > choose:
    print("you lose")
elif choose == 2 and computer_choice == 0:
    print("you lose")
elif choose == computer_choice:
    print("its a draw")
elif choose > computer_choice:
    print("you win")
elif choose == 0 and computer_choice == 2:
    print("you win")