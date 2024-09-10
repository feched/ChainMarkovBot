import numpy as np


def ChainMarkovForFiles(text):
    # переменная, где хранятся входные данные
    text = open(text, encoding='utf8').read()
    # количество слов в самом итоговом тексте
    n_words = 100
    # корпус, сюда будет сохранятся результат
    corpus = text.split()  # разбивает весь текст на слова

    # генератор, которая разбивает все слова на пары
    def make_pairs(corpus):
        for i in range(len(corpus) - 1):
            yield corpus[i], corpus[i + 1]

    # сохраняем наши пары в список
    pairs = make_pairs(corpus)
    # создаем словаарь
    word_dict = {}

    # перебираем все наши пары из нашего списка
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    # слйчайно выбираем первое слово из корпуса
    # с него мы начнем
    first_word = np.random.choice(corpus)

    # пока в нашем первом словне нет больших букв
    while first_word.islower():
        # то выбираем новое слово
        first_word = np.random.choice(corpus)

    # делаем наше первое слово первым звеном
    chain = [first_word]

    # цикл, который создает текст длинной в n_words
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    # вывод
    return ' '.join(chain)


def ChainMarkovForText(input_text):
    # количество слов в самом итоговом тексте
    n_words = 100
    # корпус, сюда будет сохранятся результат
    corpus = input_text.split()  # разбивает весь текст на слова

    # генератор, который разбивает все слова на пары
    def make_pairs(corpus):
        for i in range(len(corpus) - 1):
            yield corpus[i], corpus[i + 1]

    # сохраняем наши пары в список
    pairs = make_pairs(corpus)
    # создаем словарь
    word_dict = {}

    # перебираем все наши пары из нашего списка
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    # случайно выбираем первое слово из корпуса
    first_word = np.random.choice(corpus)

    # пока в нашем первом слове нет больших букв
    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    for i in range(n_words):
        last_word = chain[-1]
        if last_word in word_dict:  # проверяем, есть ли текущее слово в словаре
            next_word = np.random.choice(word_dict[last_word])
            chain.append(next_word)
        else:
            break  # если слов больше нет, выходим из цикла

    return ' '.join(chain)  # возвращаем результат
