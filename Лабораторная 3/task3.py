# TODO  Напишите функцию count_letters


def count_letters(text):
    counted_letters = dict()  # Словарь, где будет храниться ответ
    for letter in text:
        if letter.isalpha():
            if letter.lower() in counted_letters:
                counted_letters[letter.lower()] += 1
            else:
                counted_letters[letter.lower()] = 1
    return counted_letters


# TODO Напишите функцию calculate_frequency


def calculate_frequency(counted_letters, letters_count):
    calculated_frequency = dict()  # Словарь, где будет храниться результат
    for letter in counted_letters:
        calculated_frequency[letter] = counted_letters[letter] / letters_count
    return calculated_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result1 = count_letters(main_str)  # Словарь, где ключ - буква, значение - количество вхождений в текст
letters_count = sum(result1.values())  # Количество букв в тексте
result = calculate_frequency(result1, letters_count)  # Словарь с частотами, ключ - буква, значение - частота
for letter in result.items():
    print(f"{letter[0]}: {letter[1]:.2f}")
