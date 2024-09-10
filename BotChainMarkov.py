# Чат бот с цепями Маркова

import telebot
import os
import ChainMarkov

bot = telebot.TeleBot('7539804440:AAHNk3lZDvXnUcG9Me3LuLwNlnl2av9YXYM')


# проверка на то, чтобы бот не отвечал на стикеры и фотографии
@bot.message_handler(content_types=['sticker', 'photo', 'animation', 'video', 'image', 'voice'])
def check(message):
    bot.send_message(message.chat.id, 'Я хочу видеть настоящий текст от 100 слов до 4096 символов!')


# создадим декоратор для обработки команды /start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, жду от тебя сообщение или txt файлик, '
                                      'на основе которого я тебе вышлю бездумный текст, '
                                      'используя Цепи Маркова')


# создадим декоратор для обработки команды /help
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Итак, просто напоминаю, что я создан для того, '
                                      'чтобы придумывать бессмысленный текст. Я жду от тебя любое сообщение '
                                      'от 100 слов до 4096 символов или же обычный txt файлик')


# создадим декоратор, который будет обрабатывать сообщение пользователя
@bot.message_handler(content_types=['text'])
def text_processing(message):
    try:
        # Подсчитываем количество слов в сообщении
        word_count = len(message.text.split())

        if word_count <= 100:
            bot.send_message(message.chat.id, 'Очень мало слов, нужно больше. Давайте от 100 слов')
        else:
            # Продолжайте обработку текста, если количество слов достаточное
            generated_text = ChainMarkov.ChainMarkovForText(message.text)
            bot.send_message(message.chat.id, f'Ваш сгенерированный текст:\n\n{generated_text}')
    except:
        bot.send_message(message.chat.id, 'В общем, я пришел к выводу, что то пошло не так')


# создадим функцию, которая берет txt файлик и выполняет алгоритм
@bot.message_handler(content_types=['document'])
def file_processing(message):
    try:
        file_info = bot.get_file(message.document.file_id)

        # Проверяем, что файл имеет расширение .txt
        if message.document.file_name.endswith('.txt'):
            # Загружаем содержимое файла
            downloaded_file = bot.download_file(file_info.file_path)

            # Запись файла во временный текстовый файл
            with open('temp.txt', 'wb') as new_file:
                new_file.write(downloaded_file)

            # Генерация текста
            generated_text = ChainMarkov.ChainMarkovForFiles("temp.txt")
            bot.send_message(message.chat.id, f'Ваш сгенерированный текст:\n\n{generated_text}')

            # Удаляем временный файл
            os.remove('temp.txt')
        else:
            bot.send_message(message.chat.id, 'Это не txt файлик')
    except:
        bot.send_message(message.chat.id, 'В общем, я пришел к выводу, что то пошло не так')


# делаем так, чтобы бот работал постоянно
bot.infinity_polling()
