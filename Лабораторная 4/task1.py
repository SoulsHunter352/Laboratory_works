import json


# TODO решите задачу
def task(file_path: str) -> float:
    """Функция принимает путь до файла"""
    with open(file_path, "r") as f:
        json_data = json.load(f)
    # Считаем сумму произведений значений по ключам score и weight для каждого словаря
    return round(sum(item["score"] * item["weight"] for item in json_data), 3)


file = "input.json"  # Имя файла
print(task(file))
