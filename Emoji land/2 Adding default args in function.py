# defining a function for generate land
import random


def generate_land(rows=10, cols=10):

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


generate_land(5, 5)
generate_land(6, 6)
generate_land()  # uses default values 10,10
generate_land(20)
