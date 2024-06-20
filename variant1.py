from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()
result = translator.translate("dog", dest="ru")
print(result.text)


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
    print("Добро пожаловать в игру")
    while True:
        # Определяемся с языком
        print("Выбираем язык игры")
        lang = input("Н")
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        print(word, "en ", word_definition)
        print("!")
        result_word = translator.translate(word, dest="ru")
        ru_word = result_word.text
        ru_definition = translator.translate(word_definition, dest="ru").text

        print(ru_word, 'ru: ', ru_definition)
        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()
