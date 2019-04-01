#while01.py
user_input = input('input something:')

while user_input != 'q' and user_input != 'Q':
    print('your input is s%', user_input)
    user_input = input('"q" or "Q" for quit:')

print('here is not while')
