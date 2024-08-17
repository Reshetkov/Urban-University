class User:
    """
    Класс пользователя, содержащий атрибуты: имя, фамилию, логин, пароль
    """
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        # if password == password_confirm:
        #     self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f'\nИмя: {self.first_name}\nФамилия: {self.last_name}\nЛогин: {self.username}\nПароль: {self.password}\n')

    def greet_user(self):
        print(f'Здравствуйте, {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts < 2:
            print('Пароли не совпадают, попробуйте ещё раз')
        else:
            print('Вы использовали все свои попытки. Повторите через 10 минут')

    def reset_login_attempts(self):
        self.login_attempts = 0

class Restaurant:
    def __init__(self):
        self.number_served = 0
    def update_number_served(self):
        self.number_served += 1

user1 = User(input('Введите имя: '), input('Введите фамилию: '), input('Введите логин: '))
while True:
    if user1.login_attempts == 2:
        break
    password1 = input('Введите пароль: ')
    password2 = input('Повторите пароль: ')
    if password1 != password2:
        user1.increment_login_attempts()
    else:
        user1.password = password1
        user1.greet_user()
        user1.describe_user()
        break

user1.reset_login_attempts()

while True:
    if user1.login_attempts == 2:
        break
    password1 = input('Введите пароль: ')
    password2 = input('Повторите пароль: ')
    if password1 != password2:
        user1.increment_login_attempts()
    else:
        user1.password = password1
        user1.greet_user()
        user1.describe_user()
        break


user2 = User(input('Введите имя2: '), input('Введите фамилию: '), input('Введите логин: '))
while True:
    if user2.login_attempts == 2:
        break
    password1 = input('Введите пароль: ')
    password2 = input('Повторите пароль: ')
    if password1 != password2:
        user2.increment_login_attempts()
    else:
        user2.password = password1
        user2.greet_user()
        user2.describe_user()
        break



restaurant = Restaurant()
print(restaurant.number_served)
restaurant.update_number_served()
print(restaurant.number_served)
restaurant.update_number_served()
print(restaurant.number_served)