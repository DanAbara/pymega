keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACK']
        ]


for row_index, row in enumerate(keys):
    print(row_index, row)
        
    for col_index, key in enumerate(row):
        print(col_index, key)


guess = ['A', 'B', 'D', 'U', 'L']
joined = ''.join(guess).lower()
print(joined)

joined2 = list(joined)
print(joined2)