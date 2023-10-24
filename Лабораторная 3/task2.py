# TODO Напишите функцию find_common_participants


def find_common_participants(first_participants, second_participants, separator=","):
    first_participants = first_participants.split(separator)  # Список первых посетителей
    second_participants = second_participants.split(separator)  # Список вторых посетителей
    # Список общих посетителей
    common_participants = list(set(first_participants).intersection(set(second_participants)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
