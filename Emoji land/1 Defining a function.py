# defining a function for generate land
import random


def generate_land(rows, cols):

    print('\nWelcome to Generate Land!')
    # rows = 10
    # cols = 10
    data = ['a', 'b', 'c', 'd', 'e', 'f']

    for row in range(rows):
        row_string = ''
        for col in range(cols):
            r = random.choice(data)
            row_string += r
        print(row_string)

    print('Generation completed!')


generate_land(5, 5)
generate_land(10, 10)
