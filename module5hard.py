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
    def __init__(self, User, Video, current_user, age):
        self.users = {}
        self.videos = {}
        self.current_user = current_user
        self.age = age

    def __repr__(self):
        return f'{self.__class__}: {self.users}'

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == hash(self.users[nickname]):
                self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = password
            self.current_user = nickname
            self.age = age
        else: print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, title, duration):
        if title not in self.videos.keys():
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
ur = UrTube({}, {}, None, None)


#while True:
user = User(input('Введите логин: '), input('Введите пароль: '), int(input('Введите возраст: ')))
ur.register(user.nickname, user.password, user.age)
ur.log_in(user.nickname, user.password)


v1 = Video('Animals World', 5)
v2 = Video('Plants', 7)
#ur.add(v1, v2)
ur.add(v1.title, v1.duration)
ur.add(v2.title, v2.duration)
ur.get_videos('Animals')
ur.watch_video('Animals World')

