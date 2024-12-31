import random

guessNumber =random.randint(1,100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100'))

        if guess<guessNumber:
            print('Too low')
        elif guess>guessNumber:
            print('Too high')
        else:
            print('Congratulations!! you guess the number')
            break

    except ValueError:
        print('please enter a valid number')