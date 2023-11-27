lst = list(map(int, input("Введите элементы списка, разделенные пробелами: ").split()))

# Вычисляем минимальный по модулю элемент списка
min_abs = min(abs(x) for x in lst)
print(f"Минимальный по модулю элемент списка: {min_abs}")

# Проверяем, есть ли в списке ноль
if 0 in lst:
    # Вычисляем сумму модулей элементов списка, расположенных после первого нуля
    first_zero = lst.index(0) # Находим индекс первого нуля
    sum_abs = sum(abs(x) for x in lst[first_zero+1:]) # Суммируем модули элементов после него
    print(f"Сумма модулей элементов списка, расположенных после первого нуля: {sum_abs}")
else:
    print("В списке нет нулевых элементов.")

# Преобразуем список так, чтобы в первой его половине располагались элементы, стоявшие в четных позициях,
#а во второй половине - элементы, стоявшие в нечетных позициях
even = lst[::2] # Берем элементы с четными индексами
odd = lst[1::2] # Берем элементы с нечетными индексами
lst = even + odd # Объединяем два списка
print(f"Преобразованный список: {lst}")