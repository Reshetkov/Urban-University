class WordsFinder:
    def __init__(self, *file):
        self.file = file

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file)):
            name = self.file[i]
            with open(name, encoding='utf-8') as file:
                all_words[name] = file.read().lower()
                for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if p in all_words[name]:
                        all_words[name] = all_words[name].replace(p, '')
                all_words[name] = all_words[name].split()
        return (all_words)

    def find(self, word):
        position = {}
        all_words = self.get_all_words()
        for i in range(len(self.file)):
            name = self.file[i]
            index = all_words[name].index(word.lower()) + 1
            position[name] = index
        return (position)

    def count(self, word):
        number = {}
        all_words = self.get_all_words()
        for i in range(len(self.file)):
            name = self.file[i]
            count = all_words[name].count(word.lower())
            number[name] = count
        return (number)
    
finder2 = WordsFinder('test_file.txt')
#finder2 = WordsFinder('test_file.txt', 'test.txt') #проверка для 2-х файлов
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего