# Math:
# 1. Найти корни квадратного уравнения ax^2 + bx + c (math.sqrt)

import math


a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
disc = math.pow(b, 2) - 4 * a * c
if disc < 0:
    print('Нет корней')
elif disc == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')

# 2. Найти площадь круга (from math import pi) Площадь = πR2.

from math import pi


r = float(input('Введите радиус: '))
s = math.pi * math.pow(r, 2)
print(f'Площадь круга = {s}')

# Counter:
# 1. Вывести элементы массива, которые встречаются только один раз (или два/три/четыре раза), причём в том порядке,
# в котором они идут в массиве.

from collections import Counter
array = [2, 3, 4, 1, 5, 7, 7, 4, 5, 3, 3, 3, 5, 7]
count = []
for key, value in Counter(array).items():
    if value == 1:
        count.append(key)
print(count)

# Дан массив a из n целых чисел. Напишите программу, которая найдет наибольшее число,
# которое чаще других встречается в массиве (т.е. если три числа встречаются одинаковое количество раз,
# нужно найти наибольшее из них).

n = int(input('Количество чисел в массиве: '))
a = [int(i) for i in input().split()]
counter = Counter(a)
result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count
print(result)


# Itertools:
# 1. Нужно составить таблицу кодовых слов для передачи сообщений,
# каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов используются пятибуквенные слова,
# в которых есть только буквы А, Т, О, М, причём буква «М» появляется ровно 1 раз.
# Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не встречаться совсем.
# Сколько различных кодовых слов можно использовать?

import itertools


k = 0
a = list(itertools.product("атом", repeat = 5))
for x in a:
    if x.count("м") == 1:
        k += 1
print(k)

# 2. Ученик составляет шестибуквенные слова путём перестановки букв “НЕБО”
# (или любого другого слова/набора букв). Сколько различных слов можно составить?

k = 0
a = list(itertools.permutations(input("Введите слово: ")))
print(len(set(a)))


# Cycle:
# Создайте функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа)
# заданное количество раз (tries) циклически. Один раз - один элемент списка.
# После вывода последнего значения последовательности процедура начнется с самого начала.
# Например, если в списке 2 элемента, а функция получила значение 3,
# то сначала выведется первый объект, потом последний, а потом опять первый.
# Результат работы функции представьте в виде строки, состоящей из tries количества символов.

from itertools import cycle


def infinite(lst, tries):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(tries):
            result += str(next(iter_lst))
    return result


print(infinite([1, 2, 3], 7))


# Обработка данных JSON:
# С помощью json модуля напишите скрипт, который считывает файл JSON,
# содержащий информацию о книгах (название, авторов, ISBN, количество страниц,
# статус публикации, тематику и т.д.), и выводит список всех книг,
# в которых количество страниц больше 500. (Файл books.json)

import json


with open('books.json') as books:
    b = json.load(books)

for book in b:
    if (book.get("pageCount")) > 500:
        print(book.get("title"))


# Манипулирование данными CSV:
# Используя модуль  csv, напишите скрипт, который читает CSV-файл,
# выполняет вычисления с данными и выводит результаты в новый CSV-файл.

# 1. Файл freshman_kgs.csv - создать столбец Weight diff,
# который будет отражать изменение веса с сентября по апрель.
# Вывести только те строки, в которых представлены респонденты мужского пола,
# чья разница в весе неотрицательна, а ИМТ в апреле больше двадцати.


import csv


freshman = []
newstring = []

with open('freshman_kgs.csv', 'r') as file:
    myfile = csv.reader(file)
    for row in myfile:
        freshman.append(row)
freshman[0].append('Weight diff')
newstring.append(freshman[0])

for i in freshman[1:]:
    diff = ((int(i[1])) - (int(i[2])))
    freshman[freshman.index(i)].append(diff)

for i in freshman[1:]:
    if i[0] == 'M' and int(i[5]) >= 0 and float(i[4]) > 20:
        newstring.append(i)

with open('new_freshman.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newstring)



# 2. Файл homes.csv, где представлена статистика по продаже домов.
# Столбцы: цена продажи и запрашиваемая цена (в тыс.долларов),
# жилая площадь, количество комнат, ванных комнат, возраст дома,
# количество акров на участке, налог (в долларах).
# Нужно рассчитать среднюю итоговую стоимость дома с восемью комнатами,
# а также создать новый столбец, в котором были бы только дома
# со стоимостью более 180 и налогом менее 3500.

homes = []
prices = []
newhomes = []

with open('homes.csv', 'r') as file1:
    homesfile = csv.reader(file1)
    for row in homesfile:
        homes.append(row)

for i in homes[1:]:
    price = (int(i[0])*1000) + int(i[8])
    i.append(price)
    if int(i[3]) == 8:
        prices.append(price)

avr = round(sum(prices) / len(prices))
avr = str(avr)
newhomes.append(avr)

for i in homes[1:]:
    if (int(i[9]) > 180000) and (int(i[8]) < 3500):
        newhomes.append(i)

with open('new_homes.csv', 'w', newline='') as newh:
    writer = csv.writer(newh)
    writer.writerow(['Avr Price', 'Required Houses'])
    writer.writerow(newhomes)

