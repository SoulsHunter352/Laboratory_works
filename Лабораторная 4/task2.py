from csv import DictReader
from json import dump

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file_path, json_file_path, values_separator=",", lines_separator="\n") -> None:
    """Функция принимает путь до файла csv и json,
    разделить значений в csv файле и разделитель строк в csv файле"""
    json_data = []  # Список словарей
    with open(csv_file_path, "r") as f:  # TODO считать содержимое csv файла
        # Чтение данных в словари
        csv_reader = DictReader(f, delimiter=values_separator, quotechar=lines_separator)
        for line in csv_reader:
            json_data.append(line)
    with open(json_file_path, "w") as f:  # TODO Сериализовать в файл с отступами равными 4
        dump(json_data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
