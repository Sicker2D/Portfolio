import math
while True:
    print("Choose an operation to complete!")
    user_input: str = input().lower()
    if user_input in ['+', 'add', 'addition']:
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number:'))
            print(f'The sum of {num1} and {num2} is {num1 + num2}')
        except ValueError:
            print('That doesn\'t seem like a valid number. Try again!')
    elif user_input in ['-', 'subtract', 'subtraction']:
            try:
                num1: float = float(input('First number: '))
                num2: float = float(input('Second number:'))
                print(f'The difference of {num1} and {num2} is {num1 - num2}')
            except ValueError:
                print('That doesn\'t seem like a valid number. Try again!')
    elif user_input in ['*', 'multiply', 'multiplication']:
            try:
                num1: float = float(input('First number: '))
                num2: float = float(input('Second number:'))
                print(f'The product of {num1} and {num2} is {num1 * num2}')
            except ValueError:
                print('That doesn\'t seem like a valid number. Try again!')
    elif user_input in ['/', 'divide', 'division']:
            try:
                num1: float = float(input('First number: '))
                num2: float = float(input('Second number:'))
                print(f'The quotient of {num1} and {num2} is {num1 / num2}')
            except ValueError:
                print('That doesn\'t seem like a valid number. Try again!')
    elif user_input in ['root']:
            try:
                    num1: float = float(input('To what root would you like to do? '))
                    num2: float = float(input(f'What number would you like to put to the {num1} root?'))
                    print(f'{num2} to the {num1} root is {num2**(1/num1)}')
            except ValueError:
                    print('That doesn\'t seem like a valid number. Try again!')
    elif user_input in ['^x']:
                try:
                    num1: float = float(input('What power would you like to do? '))
                    num2: float = float(input(f'What number would you like to put to the {num1} power?'))
                    print(f'{num2} to the {num1} power is {num2**num1}')
                except ValueError:
                    print('That doesn\'t seem like a valid number. Try again!')

    else: 
        print('I\'m sorry! That dosen\'t seem like a valid operation. Try again!')