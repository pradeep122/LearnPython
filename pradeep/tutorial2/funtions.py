
def greet():
    print('Hi There!')
    print('Welcome aboard')


def greet_user(first_name, last_name):
    print(f'Hi {first_name}  {last_name}!')
    print('Welcome aboard')


print('Start')
greet()
greet_user('Pradeep', 'Dantuluri')
greet_user(last_name='Kalidindi', first_name='Swetha')
print('Finish')


def square(number):
    return number * number


print(square(3))
