import random

while True:
    print(f'A random whole number from 1-100 will be generated and you will make a guess. You will then be told if the number is higher or lower than your guess.')
    truenum: float = int(random.randint(1, 100))
    for i in range(1000):
        try:
            guess: float = int(input())
            if (guess < truenum):
                print('Higher')
            elif (guess > truenum):
                print('Lower')
            elif (guess == truenum):
                print('Correct')
                print('Would you like to play again?')
                user_input: str = input().lower()
                if (user_input == ['yes', 'y', 'sure', 'yea', 'yeah']):
                    break
                elif (user_input == ['no', 'n']):
                    exit()
                else:
                    print('Unrecongized input shutting down')
                    exit()
        except ValueError:
            print('That dosen\'t seem like a whole number. Please try again!')
