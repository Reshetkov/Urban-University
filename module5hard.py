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
        self.users = {}
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
        return list

    def watch_video(self, title):
        for key in self.videos:
            if key == title:
                if self.current_user != None:
                    if self.age >= 18:
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

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')