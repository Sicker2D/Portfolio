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
    else: 
        print('I\'m sorry! That dosen\'t seem like a valid operation. Try again!')