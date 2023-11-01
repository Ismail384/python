
import random
 
# generate computer choice
def computer_play():
    computer_choice=['rock', 'paper', 'scissor']
    picked_option =random.choice(computer_choice)
    return picked_option



# capture the user's turn

def user_play():
    print('pick a choice:')
    user_choice = input('enter your choice: ').lower()
    return user_choice

# determine the winner

def determine_winner():
    picked_option = computer_play()
    user_choice = user_play()

    print('the computer chose',picked_option ,'and the user chose' ,user_choice)

    if picked_option == user_choice:
        print('there is a tie')

    elif(picked_option == 'rock' and user_choice == 'scissor') or (picked_option == 'scissor' and user_choice == 'paper') or (picked_option == 'paper' and user_choice =='rock'):
        print('the computer wins')

    else:
        print(' you win')
    

    

determine_winner()
