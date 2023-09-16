import random

rows = 10
cols = 20
data = [1, 2, 3, 4, 5, 6]

for col in range(cols):
    row_string = ''
    for row in range(rows):
        r = random.choice(data)
        row_string += str(r)

    print(row_string)

print('Generation completed')
