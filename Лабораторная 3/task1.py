# TODO Напишите функцию для поиска индекса товара

def find_item_in_list(items: list, item):
    for i in range(len(items)):
        if items[i] == item:  # Проверяем, является ли элемент искомым
            return i


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_in_list(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
