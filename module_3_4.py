same_words = []
other_words = []

def f_list(z):
    global other_words
    for i in range(z):
        word = (input(f'Введите элемент {i+1} Вашего списка: '))
        word_lower = word.lower()
        other_words.append(word)
        other_words.append(word_lower)
    return other_words


def single_root_words(root_word, *other_words):
    global same_words
    n = len(other_words)
    for i in range(0, n, 2):
        if root_word in other_words[i + 1]:
           same_words.append(other_words[i])
        if other_words[i + 1] in root_word:
           same_words.append(other_words[i])
    return same_words



x = input('Введите обязательное слово: ').lower()
number = int(input('Сколько элементов будет содержать Ваш список?: '))
other_words = f_list(number)
single_root_words(x, *other_words)
print(list(set(same_words))) # чтобы одинаковые слова не повторялись