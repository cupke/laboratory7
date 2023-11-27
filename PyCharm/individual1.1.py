def find_indexes_with_comprehension(arr, target):
    # Используется List Comprehension для создания списка индексов, в которых найден целевой элемент
    indexes = [i for i, x in enumerate(arr) if x == target]

    return indexes if indexes else "Элемент не найден в списке"

user_list = input("Введите элементы списка через пробел: ").split()
user_list = [int(item) for item in user_list] # Преобразование введенных строк в целые числа
element_to_find = int(input("Введите элемент, который нужно найти: "))
# Вызов функции с использованием List Comprehension для поиска индексов элемента в списке
result_with_comprehension = find_indexes_with_comprehension(user_list, element_to_find)

print(f"Индексы элемента {element_to_find}: {result_with_comprehension}")
