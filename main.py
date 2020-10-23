

# Game rock-paper-scissors
import random


player = input('Enter your choice:')
computerCode = random.randint(0, 2)

if computerCode == 0:
    computer = 'rock'
elif computerCode == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f'computer has a {computer}')

if player == computer:
    print('Draw')
else:
    if player == 'rock':
        if computer == 'paper':
            print('Lose')
        else:
            print('Win')
    elif player == 'paper':
        if computer == 'scissors':
            print('Lose')
        else:
            print('Win')
    elif player == 'scissors':
        if computer == 'rock':
            print('Lose')
        else:
            print('Win')

