import random

print('Enter rock, paper or scissors: ')
user_input = input()
possible_answers = ['rock', 'paper', 'scissors']
computer_answer = possible_answers[random.randint(0, 2)]

computer_score = 0
user_score = 0
games_played = 0
while user_input != 'end':
    if user_input == 'rock':
        if computer_answer == 'paper':
            computer_score += 1
            print('Computer won! Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'scissors':
            user_score += 1
            print('User won!')
            print('Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'rock':
            print('Draw! Enter rock, paper or scissors again: ')
            user_input = input()
            games_played += 1
            computer_answer = possible_answers[random.randint(0, 2)]
    elif user_input == 'paper':
        if computer_answer == 'scissors':
            computer_score += 1
            print('Computer won!')
            print('Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'rock':
            user_score += 1
            print('User won!')
            print('Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'paper':
            print('Draw! Enter rock, paper or scissors again: ')
            user_input = input()
            games_played += 1
            computer_answer = possible_answers[random.randint(0, 2)]
    elif user_input == 'scissors':
        if computer_answer == 'rock':
            computer_score += 1
            print('Computer won!')
            print('Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'paper':
            user_score += 1
            print('User won!')
            print('Enter another one: ')
            user_input = input()
            computer_answer = possible_answers[random.randint(0, 2)]
            games_played += 1
        if computer_answer == 'scissors':
            print('Draw! Enter rock, paper or scissors again: ')
            user_input = input()
            games_played += 1
            computer_answer = possible_answers[random.randint(0, 2)]
    else:
        break


if computer_score > user_score:
    print('You lose! Try again! Your score is ', user_score,  ' and computer score is ', computer_score,
          ' he won ', computer_score-user_score, ' games more.')
elif user_score > computer_score:
    print('You won! Your score is ', user_score, ' and computer score is ', computer_score,
          ' you won ', user_score - computer_score, ' games more.')
else:
    print('Draw! You have played ', games_played, ' games')