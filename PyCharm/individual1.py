# Функция для поиска индексов заданного элемента в списке с использованием циклов
def find_indexes_with_loops(arr, target):
    indexes = []
    # Итерация по списку с использованием enumerate для получения индекса и значения
    for index, value in enumerate(arr):
        if value == target:
            indexes.append(index) #добавляем индекс в список индексов

    return indexes if indexes else "Элемент не найден в списке"

list = input("Введите элементы списка через пробел: ").split()
list = [int(item) for item in list] #Преобразование введенных строк в целые числа
element_to_find = int(input("Введите элемент, который нужно найти: "))
# Вызов функции с циклами для поиска индексов элемента в списке
result_with_loops = find_indexes_with_loops(list, element_to_find)

print(f"Индексы элемента {element_to_find}: {result_with_loops}")
