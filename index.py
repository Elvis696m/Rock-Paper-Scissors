import random
choices = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(choices)
choice = (input('Enter your choice: ')).capitalize()
if choice == computer_choice:
    print('Its a tie!')
elif choice == 'Rock' and computer_choice == 'Paper':
    print('You lose!')
elif choice == 'Paper' and computer_choice == 'Rock':
    print('You win!')
elif choice == 'Scissors' and computer_choice == 'Rock':
    print('You lose!')
elif choice == 'Rock' and computer_choice == 'Scissors':
    print('You win!')
elif choice == 'Paper' and computer_choice == 'Scissors':
    print('You lose!')
elif choice == 'Scissors' and computer_choice == 'Paper':
    print('You win!')
else:
    print('Try choosing Rock, Paper, or Scissors!')
