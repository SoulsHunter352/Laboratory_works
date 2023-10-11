numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_none_element = numbers.index(None)  # Находим индекс None элемента
numbers_sum = sum(numbers[:index_none_element]) + sum(numbers[index_none_element + 1:])
average = numbers_sum / len(numbers)  # Среднее арифметическое чисел массива
numbers[index_none_element] = average  # Присваиваем значение None элементу
print("Измененный список:", numbers)
