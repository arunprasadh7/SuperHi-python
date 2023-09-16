# input function
import random


def generate_land(cols=10, rows=10):

    print('\nWelcome to Generate Land!')
    # rows = 10
    # cols = 10
    print(f'Generating landscape for {cols} by {rows}.\n')
    data = ['a', 'b', 'c', 'd', 'e', 'f']

    for row in range(rows):
        row_string = ''
        for col in range(cols):
            r = random.choice(data)
            row_string += r
        print(row_string)

    print('Generation completed!')


cols = int(input('How many columns ?'))
rows = int(input('How many rows ?'))

generate_land(cols, rows)
