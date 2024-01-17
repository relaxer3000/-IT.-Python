# TODO Напишите функцию для поиска индекса товара
def fun(find, items):
    for i in items:
        if find == i:
            c = items.index(i)
            return c
    else:
            return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = fun(find_item, items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
