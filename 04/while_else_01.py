#while_else_01.py
user_input = input('input something:')

while user_input != 'q' and user_input != 'Q':
    if user_input == 'quit':
        break
    print('your input is s%', user_input)
    user_input = input('"q" or "Q" for quit:')
else:
    print('end of the loop!')

print('here is not while')
