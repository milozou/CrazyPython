#while_True_01.py
print('input something:')

while True:
    user_input = input('"q" or "Q" for quit:')
    if user_input != 'q' and user_input != 'Q':
        break
    print('your input is s%', user_input)
    
print('here is not while')
