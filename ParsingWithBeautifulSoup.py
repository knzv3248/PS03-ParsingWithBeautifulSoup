from bs4 import BeautifulSoup
import requests
from googletrans import Translator      # импоритруем переводчик

translator = Translator()

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    response = requests.get(url)
    # Создаём объект Soup
    soup = BeautifulSoup(response.content, "html.parser")
    # Получаем слово. text.strip удаляет все пробелы из результата
    english_word = soup.find("div", id="random_word").text.strip()

    # Получаем описание слова
    word_definition = soup.find("div", id="random_word_definition").text.strip()

    # Чтобы программа возвращала словарь
    return {
        "english_word": english_word,
        "word_definition": word_definition
    }

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру по уадыванию слова по его определению")
    print("Внимание!\nИгра осуществляется на русском языке!\nПри необходимости измените раскладку клавиатуры.")

    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        ru_word = translator.translate(word, dest="ru").text
        ru_definition = translator.translate(word_definition, dest="ru").text

        # Начинаем игру
        print(f"Значение слова - {ru_definition}")
        user = input("Что это за слово? ")
        if user == ru_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово: {ru_word}")
            print(f"Не огорчайтесь! Возможно ошибка возникла из-за машинного перевода английского слова {word}.")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again != "д":
            print("Спасибо за игру!")
            break
word_game()
