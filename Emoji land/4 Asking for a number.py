import random


def generate_land(cols=5, rows=5):
    print('\nWelcome to EMOJI LAND!!!')
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f'Generating landscape for {cols} by {rows}.')
    for row in range(rows):
        row_string = ''
        for col in range(cols):
            r = random.choice(data)
            row_string += r
        print(row_string)
    print('Generation completed.')


def ask_for_number(question):
    answer = input(question)
    if answer.isnumeric():
        return int(answer)
    else:
        print('Non-numeric value detected.\nEnter numeric values and try again.')
        quit()


cols = ask_for_number('How many cols?')
rows = ask_for_number('How many rows?')
generate_land(cols, rows)
