def get_number_input(min, max):
    while True:
        user_input = input()
        try:
            user_int = int(user_input)
            if user_int < min or user_int > max:
                print(f'Please enter a number between {min} and {max}')
                continue
            return user_int
        except ValueError:
            print('You did not enter a number.')


def yes_no(text):
    name_answer = input(text).lower()
    yes_or_no = ['y', 'yes', 'no', 'n']
    while name_answer not in yes_or_no:
        print('Please input yes(y) or no(n)')
        name_answer = input('y/n: ').lower()
        print(name_answer)
    if name_answer == 'no' or name_answer == 'n':
        return False
    elif name_answer == 'yes' or name_answer == 'y':
        return True


def get_string(text):
    while True:
        string = input(text).strip()
        if string == '':
            print('Please enter a text')
        else:
            return string
