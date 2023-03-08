import random as rand

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

#code random
machine_code = rand.randint(0,2)
if machine_code == 0:
    machine_type = rock
elif machine_code == 1:
    machine_type = paper
elif machine_code == 2:
    machine_type = scissors

#user random
code_of_play = int(input('what do you choose? Type 0 for rock, 1 for papper or 2 for scissors. '))
if code_of_play == 0:
    Type_of_play = rock
elif code_of_play == 1:
    Type_of_play = paper
elif code_of_play == 2:
    Type_of_play = scissors

# comparison
print(Type_of_play, '\n computer chose: \n{}'.format(machine_type))
if machine_code == code_of_play:
    print('Draw!')
elif (machine_code ==0 and code_of_play == 2) or (machine_code == 1 and code_of_play == 0) or (machine_code ==2 and code_of_play == 1):
    print('You Lose!')
else:
    print('You Won!')