import random

while True:
    my_answer = (input('Choose from these choices : "Rock", "Paper", "Scissor" '))
    my_answer = my_answer.lower()
    
    if my_answer != 'rock' and my_answer != 'paper' and my_answer != 'scissor':
        print('Please choose only from given choices')
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissor'])
    print(f'Computer chose : {computer_choice}')
    
    if my_answer == computer_choice:
        print('You Tied')
        # ask = input('Do you want play again ? \n')
        # if ask.lower() == 'yes':
        #     break
        # else:
        #     break
        continue
    if my_answer == 'rock' and computer_choice == 'scissor':
        print('You won')
        # askagain = input('Do you want to play again ? \n')
        # if askagain.lower() == 'yes':
        #     break
        # else:
        continue
    if my_answer == 'paper' and computer_choice == 'rock':
        print('You Won')
        break
    if my_answer == 'scissor' and computer_choice == 'paper':
        print('You Won')
        break
    else:
        print('You lose, Try Again!')
    

    