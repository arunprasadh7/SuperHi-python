# adding noise
import random
from termcolor import colored  # pip install termcolor module
from opensimplex import noise3


def generate_land(cols=5, rows=5):
    print('\nWelcome to EMOJI LAND!!!')
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    seed = random.randint(0, 100)

    print(f'Generating landscape for {cols} by {rows}.')
    for row in range(rows):
        row_string = ''
        for col in range(cols):
            n = noise3(row / rows, col / cols, seed)
            n *= 10
            n = round(n)
            n = n % len(data)
            # print(n)
            # r = random.choice(data)
            row_string += data[n]
        print(row_string)
    print('Generation completed.')


def ask_for_number(question):
    count = 0
    while count < 3:
        answer = input(colored(question + '\n', 'green'))
        if answer.lower() == 'quit':
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored(
                'Non-numeric value detected.\nEnter numeric values and try again.', 'yellow'))
            count += 1
    print(colored('This isn\'t fun anymore.', 'red'))
    quit()


cols = ask_for_number('How many cols?')
rows = ask_for_number('How many rows?')

generate_land(cols, rows)
