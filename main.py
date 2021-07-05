import matplotlib.pyplot as plt
import re
from datetime import datetime, date


def bmi(weight, height):
    b_m_i = weight / height ** 2
    return f'{b_m_i:.2f} kg/m2'


def register_weight():
    msg = 'Enter your weight in Kg: '
    weight = validate_user_input(2, msg)
    new_reg = f'Weight: {weight}Kg ' + define_date() + "\n"
    print('Register added successfully', new_reg, sep="\n")
    upload_register(new_reg)
    return True


def define_date():
    msg = '''
a: Select for define your own date
b: Select for system define the current date
    
Select your option: '''
    user_input = validate_user_input(0, msg)
    while user_input.lower() not in ('a', 'b'):
        user_input = validate_user_input(0, msg)

    if user_input == 'b':
        return datetime.now().strftime('%Y-%B-%d %H:%M:%S')

    year = validate_user_input(1, 'Enter the year (eg. 2019): ')
    while not 2015 < year <= date.today().year:
        print('Year out of range')
        year = validate_user_input(1, 'Enter the year (eg. 2019): ')

    month = validate_user_input(1, 'Enter the month (1-12): ')
    while not 1 < month <= 12:
        print('Month out of range')
        month = validate_user_input(1, 'Enter the month (1-12): ')

    day = validate_user_input(1, 'Enter the day (eg. 1-31): ')
    while not 1 < day <= 31:
        print('Day out of range')
        day = validate_user_input(1, 'Enter the day (eg. 16): ')

    return datetime(year, month, day).strftime('%Y-%B-%d %H:%M:%S')


def upload_register(register):
    with open('weight_register', 'a') as file:
        file.write(register)


def validate_user_input(ty_pe, msg):
    # Type: 0 -> string, 1 -> integer, 2 -> float
    user_input = input(msg)

    if ty_pe == 0:
        try:
            assert user_input.isalpha()
        except AssertionError:
            msg = '''Enter only letter
Enter your value again: '''
            return validate_user_input(ty_pe, msg)
        else:
            return user_input

    if ty_pe == 1:
        try:
            int(user_input)
        except ValueError:
            msg = '''Enter only numbers!!
Enter your value again: '''
            return validate_user_input(ty_pe, msg)
        else:
            return int(user_input)

    if ty_pe == 2:
        try:
            float(user_input)
        except ValueError:
            msg = '''Enter only numbers separate with "." eg 70.5
Enter your value again '''
            return validate_user_input(ty_pe, msg)
        else:
            return float(user_input)


def check_weight():
    with open('weight_register', 'r') as file:
        content = file.read()
    return content


def graph_data(info):
    with open(info, 'r') as file:
        content = file.readlines()
    expresion_x = '[0-9]*\.[0-9]*'
    expresion_y = '[0-9]*\-[a-zA-Z]+\-[0-9]*'
    weight_y = [float(re.findall(expresion_x, item)[0]) for item in content]
    time_x = [re.findall(expresion_y, item)[0] for item in content]
    plt.plot(time_x, weight_y)
    plt.xlabel('Month')
    plt.ylabel('Weight')
    plt.show()


message = '''!!!Welcome to your fitness app!!!
a) Register a weight measure.
b) Show weight registered
z) Exit app.'''

print(message)
msgs = 'Choice an option: '
user_selection = validate_user_input(0, msgs)
if user_selection == 'a':
    register_weight()
if user_selection == 'b':
    print(check_weight())
    print(graph_data('weight_register'))









