# создание списка  #####################################################################################################
# a = [2, 3, 4]
# a = list([1, 2, 3])
# list(range(10))  # генератор списка

# методы списка  #######################################################################################################

# .append()  # добавить в конец (один элемент)
# .extend([5, 5])  # добавить в конец (несколько элементов)
# .insert(3, 'a')  # вставить в определенное место
# .index('i', 5, 7)  # индекс элемента  (необязат. (5-нач., 7-кон.), возвращает первое вхождение, нет элемента - ошибка)
# .pop(0) - получить элемент по индексу [0], удаляя его из последовательности (по умолчанию () - последний)
# my_list[1] = 200  # заменить в списке
# del my_list[5]  # удалить элемент (с конкретного места)
# my_list.remove('s')  # находит первый по порядку элемент 's'
# my_list.count('d')  # количество элементов в списке
# min(my_list), max(my_list), sum(my_list)  # найти мин, макс, сумму (для списка чисел)
# my_list.sort()  # сортировать список
# sorted(my_list)  # если не надо изменить сам список (создает в памяти отсортированную копию)

#   zip() - profit = [100, 20]
#   days = ['пн', 'вт']
#   res = zip(profit, days)
#   print(list(res)) или res = list(zip(profit, days)) или print(dict(zip(days, profit)))
# ___сортировка по второму элементу: work_list.sort(key=lambda x: x[1]) или lst.sort(key=itemgetter(1)) с from operator import itemgetter
# ___получить элемент по индексу удаляя его из последовательности: dots = [segments.pop(0)[1]] for l, r in segments:

# Метод isupper() проверяет, все ли символы в строке находятся в верхнем регистре.
# Метод не принимает никаких параметров
# Метод в Python возвращает: Истинно, если все символы в строке являются прописными. False, если какие-либо символы в
# строке являются строчными.
a = 'sdf'
a.isupper()
print(a)


# Хранение в памяти
# При создании списка, в памяти резервируется пустая область. С одной стороны, это ничем не отличается от создания любого
# другого типа данных, но разница в том, что содержимое list может меняться:
# numbers = [1, 2]
# numbers[1] = 3
# # обновлённый список: [1, 3]
# До замены элемента последовательности print(numbers[1]) выведет 2, а после замены — 3.
# Создание списка в Python
# Это можно сделать несколькими способами, например перечислением элементов списка в квадратных скобках:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# При этом единица будет на позиции 0, то есть print(numbers[0]) выведет 1.
# Также можно использовать обработку итерируемого объекта функцией list(). Пусть у нас будет некоторая строка, тогда:
# list('tproger')
# # ['t', 'p', 'r', 'o', 'g', 'e', 'r']
# Также существуют генераторы списков, которые позволяют применить заданное выражение к каждому элементу
# последовательности. Допустим, необходимо создать list, состоящий из чисел от 1 до 5 включительно:
# numbers = [i for i in range(1,6)]
# # [1, 2, 3, 4, 5]
# Срезы (slice) списка
# Срезы позволяют получить некое подмножество значений. Следующий код вернёт список с элементами, начиная индексом 0 и не
# включая при этом индекс 2 и выше:
# numbers = [1, 5, 9, 6]
# print(numbers[0:2])
# # вывод [1, 5]
# Далее выведем всё, за исключением элемента на позиции 3:
# print(numbers[:3])
# # вывод [1, 5, 9]
# А теперь начиная с индекса 1 и до конца:
# print(numbers[1:])
# # вывод [5, 9, 6]
# Операции над списками Python
# x in l — true, если элемент x есть в списке l;
# x not in l — true, если элемент x отсутствует в l;
# l1 + l2 — объединение двух списков;
# l * n , n * l — копирует список n раз;
# len(l) — количество элементов в l;
# min(l) — наименьший элемент;
# max(l) — наибольший элемент;
# sum(l) — сумма чисел списка;
# for i in list() — перебирает элементы слева направо.
# Методы списков Python
# Index
# Возвращает положение первого совпавшего элемента. Поиск совпадения происходит слева направо. Пример:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.index(1))
# # вывод 0: первая найденная единица на позиции 0
# Count
# Данный метод считает, сколько раз указанное значение появляется в списке Python:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.count(1))
# # вывод 3, потому что единица встречается 3 раза
# Append
# Добавляет указанное значение в конец:
# numbers = [1, 5, 9, 6]
# numbers.append(3)
# # обновлённый список: [1, 5, 9, 6, 3]
# Sort
# Сортирует список в Пайтоне. По умолчанию от меньшего к большему:
# numbers = [1, 5, 9, 6]
# numbers.sort()
# # обновлённый список: [1, 5, 6, 9]
# Также можно сортировать последовательность элементов от большего к меньшему:
# numbers = [1, 5, 9, 6]
# numbers.sort(reverse = true)
# # обновлённый список: [9, 6, 5, 1]
# Insert
# Вставляет элемент перед указанным индексом:
# numbers = [1, 5, 9, 6]
# numbers.insert(3, [2, 3])
# # обновлённый список: [1, 5, 9, [2, 3], 6]
# Remove
# Удаляет первое попавшееся вхождение элемента в списке Python:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# numbers.remove(1)
# # обновлённый список: [5, 9, 6, 1, 2, 1]
# Extend
# Подобно методу append(), добавляет элементы, но преимущество метода extend() в том, что он также позволяет добавлять
# списки:
# numbers = [1, 5, 9, 6]
# numbers.extend([2, 3])
# # обновлённый список: [1, 5, 9, 6, 2, 3]
# Pop
# А данный метод удаляет элемент в конкретно указанном индексе, а также выводит удалённый элемент. Если индекс не указан,
# метод по умолчанию удалит последний элемент:
# numbers = [1, 5, 9, 6]
# numbers.pop(1)
# # получаем:
# # 5
# # [1, 9, 6]
# Join
# Преобразовывает список в строку. Разделитель элементов пишут в кавычках перед методом, а сам список Питона должен
# состоять из строк:
# mylist = ['сайт', 'типичный', 'программист']
# print(', '.join(mylist))
# # вывод 'сайт, типичный, программист'