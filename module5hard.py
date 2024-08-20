class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = password

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration

class UrTube:
    def __init__(self, User, Video, current_user):
        self.users = {'1': '1'}
        self.videos = {}
        self.current_user = current_user

    def __repr__(self):
        return f'{self.__class__}: {self.users}'

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == hash(self.users[nickname]):
                self.current_user = nickname
            else:
                print('Пароль неверен')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = password
            self.current_user = nickname
            self.age = age
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *v):
        for i in range(len(v)):
            title = v[i].title
            duration = v[i].duration
            self.videos[title] = duration

    def get_videos(self, keyword):
        list = []
        self.videos_temp = {i.lower(): self.videos[i] for i in self.videos}
        for key in self.videos_temp:
            if keyword.lower() in key:
                list.append(key)

    def watch_video(self, title):
        for key in self.videos:
            if key == title:
                if self.current_user != None:
                    if user.age >= 18:
                        for i in range(1, self.videos[title] + 1):
                            print(i)
                            time.sleep(1)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')


import time
ur = UrTube({}, {}, None)

N = int(input('Сколько будет пользователей?: '))
i = 1
while i <= N:
    i += 1
    ur.log_out()
    choiсe = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
    if choiсe == 1:
        user = User(input('Введите логин: '), input('Введите пароль: '), 18)
        ur.log_in(user.nickname, user.password)
    if choiсe == 2:
        user = User(input('Введите логин: '), input('Введите пароль: '), int(input('Введите возраст: ')))
        ur.register(user.nickname, user.password, user.age)

print(ur.users)
v1 = Video('Animals World', 5, 0, False)
v2 = Video('Plants', 7, 0, False)
ur.add(v1, v2)
ur.get_videos('Animals')
ur.watch_video('Animals World')