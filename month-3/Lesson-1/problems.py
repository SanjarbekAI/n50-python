import csv, os


def add_user(full_name, email, phone_number):
    try:
        with open('users/users.csv', 'a') as csvfile:
            data = f"{full_name}, {email}, {phone_number}"
            csvfile.write(data)
    except FileNotFoundError:
        os.mkdir('users')
        with open('users/users.csv', 'w', newline='') as csvfile:
            column_names = "full_name, email, phone_number"
            csvfile.write(column_names)
        add_user(full_name, email, phone_number)
    except RecursionError:
        print('We have some problems')
        return False
    except BaseException as exc:
        print(f'We have some problems {exc}')
        return False
    return True


def register_user():
    full_name = input('Enter your full name: ')
    email = input('Enter your email: ')

    while '@' not in email:
        email = input('Enter your email: ')
    phone_number = 0
    try:
        phone_number = int(input('Enter your phone number: '))
    except ValueError:
        print('Invalid phone number ')
        register_user()

    result = add_user(full_name, email, phone_number)
    if result:
        print("Thank you for registering")
    else:
        print("Sorry we have some problems please try again later")


register_user()

products = {
    'apple': 1200,
    'non': 200,
    'suv': 100,
    'qon': 12020,
}


