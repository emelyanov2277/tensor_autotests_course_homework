# # #Задания на списки (lists) в Python
# # Создание и вывод списка: Создайте список из 5 ваших любимых фруктов. Выведите весь список на экран.
# l = ['fera', 'mera', 'dita']
# print(*l)

# # Доступ к элементам: У вас есть список numbers = [10, 20, 30, 40, 50]. Выведите второй элемент списка (ожидаемый вывод: 20).
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1])

# Добавление элементов: Возьмите пустой список animals = []. Добавьте в него три элемента: "cat", "dog", "bird" с помощью метода append(). Выведите список.
# animals = []
# print(animals)
# animals.append('cat')
# print(*animals)

# Удаление элементов: У вас есть список colors = ["red", "blue", "green", "yellow"]. Удалите элемент "blue" с помощью метода remove(). Выведите обновленный список.
# colors = ["red", "blue", "green", "yellow"]
# print(colors)
# colors.remove('blue')
# print(colors)

# Срез списка: Из списка letters = ['a', 'b', 'c', 'd', 'e'] выведите срез с второго по четвертый элемент (ожидаемый вывод: ['b', 'c', 'd']).
# letters = ['a', 'b', 'c', 'd', 'e']
# print(*letters[1:4])

# Длина списка: Создайте список из 4 чисел. Выведите длину списка с помощью функции len().
# l=[1,2,3,4]
# print(len(l))

# Сортировка: У вас есть список scores = [85, 92, 78, 95, 88]. Отсортируйте его по возрастанию и выведите.
# scores = [85, 92, 78, 95, 88]
# print(sorted(scores))



# #Задания на кортежи (tuples) в Python
# Создание и вывод кортежа: Создайте кортеж из 3 цветов: "red", "green", "blue". Выведите весь кортеж.
# col=("red", "green", "blue")
# print(*col)

# Доступ к элементам: У вас есть кортеж days = ("Monday", "Tuesday", "Wednesday"). Выведите первый элемент (ожидаемый вывод: "Monday").
# days = ("Monday", "Tuesday", "Wednesday")
# print(days[0])

# Длина кортежа: Создайте кортеж из 5 чисел. Выведите его длину с помощью len().
# days = ("Monday", "Tuesday", "Wednesday")
# print(len(days))

# Распаковка кортежа: У вас есть кортеж person = ("Alice", 25, "Engineer"). Распакуйте его в три переменные: name, age, job. Выведите каждую переменную.
# person = ("Alice", 25, "Engineer")
# name, age, job = person
# print(name, age, job)

# Конкатенация кортежей: Создайте два кортежа: tuple1 = (1, 2) и tuple2 = (3, 4). Объедините их в один кортеж и выведите.
# tuple1, tuple2 = (1, 2), (3, 4)
# print(tuple1+tuple2)


# # Проверка наличия элемента: У вас есть кортеж fruits = ("apple", "banana", "cherry"). Проверьте, есть ли в нем "banana" с помощью оператора in, и выведите True или False.
# fruits = ("apple", "banana", "cherry")
# result = 'banana' in fruits
# print(result)

# Преобразование списка в кортеж: Возьмите список [10, 20, 30], преобразуйте его в кортеж с помощью tuple() и выведите.
# ls = [10, 20, 30]
# print(tuple(ls))
# print(type(tuple(ls)))
