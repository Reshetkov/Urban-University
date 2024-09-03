class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = password

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def __repr__(self):
        return f'{self.__class__}: {self.users}'

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname].password == password:
                self.current_user = nickname
            else:
                print('Пароль неверен')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *v):
        for video in v:
            self.videos[video.title] = video

    def get_videos(self, keyword):
        return [title for title in self.videos if keyword.lower() in title.lower()]

    def watch_video(self, title):
        if title in self.videos:
            if self.current_user is not None:
                user_age = self.users[self.current_user].age
                video = self.videos[title]
                if video.adult_mode and user_age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(video.duration + 1):
                        print(f'{i}')
                        time.sleep(1)
                    print('Конец видео')
                print('Видео не найдено')

import time
ur = UrTube()

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