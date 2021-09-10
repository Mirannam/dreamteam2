# '''
# Находим минимальное положительное целое число, которого нет в списке.
# Если список содержит только отрицательные числа, верните 1.
# Все элементы являются целыми числами:
# Пример: [1,2,3,4,6] - Ответ 5
# Пример: [1,2,3] - Ответ 4
# Пример: [-1, -2, -6] - Ответ 1
# '''
import itertools

import more_itertools

# num1 = [1,2,3,4,6]
# def num():
#     print(next(i for i in itertools.count() if i not in num1 and i >0 ))
#     for i in num1:
#         if i < 0:
#             print(1)
# num()
# # """
# Попросить пользователя ввести текст. В результате вывести процент букв
# в верхнем регистре (заглавные) и в нижнем регистре (прописные).
# def string_test(s):
#     d={"UP":0, "LOW":0}
#     for c in s:
#         if c.isupper():
#            d["UP"]+=1
#         elif c.islower():
#            d["LOW"]+=1
#         else:
#            pass
#     print ("Ваше слово : ", s)
#
#     y = (d['UP'] +d['LOW'])
#     up = d['UP']/y*100
#     low = d["LOW"]/y*100
#     print("Количество Букв с большой буквой : ", up, '%')
#     print("Количество Букв с маленькой буквой : ", low, '%')
# string_test(input('Введите текст:'))
# """



# """
# "Аналог шифра цезаря ". Программа должна запрашивать элементы списка через пробел.
# После чего пользователь должен ввести значение для сдвига элементов списка.
# Значение может быть как положительным, так и отрицательным. Если значение положительное,
# элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести на экран:
# Введенные данные: [5,7,9,10,2], 2
# Результат:        [9,10,2,5,7]
# def cezar():
#     a = input()
#     d = int(input())
#     b = a.split()
#     for i in range(len(b)):
#         b[i] = int(b[i])
#         if i > 0:
#             c = b[-d:] + b[:-d]
#         elif i < 0:
#             c  = b[d:] + b[:d]
#     print(c)
# cezar()


# # lst = lst[2:] + lst[:2]
# # lst = lst[-1:]+lst[:-1]

# """


# """
# "Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. Попросите пользователя ввести страну или ключ и выдайте ему результат."
# d = {'1': 'kyrgyzstan', '2': 'kazahstan', '3': 'belgium'}
# value = input('введите ключ или страну')
# def get_key(d, value):
#     for k, v in d.items():
#         if k == value:
#             return k, v
#
# def get_value(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k,v
# print(get_key(d, value))
#
# print(get_value(d, value))

"""



# """
# 'С помощью lambda выведите числа фибоначи'
# def fibonacci(count):
#     sequence = [0, 1]
#
#     any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))
#
#     return sequence[:count]
#
# print(fibonacci(10))
# """

# """
# 'С помощью рекурсии выведите факториал'


# def fac(n):
#
#     if n == 0:
#         return 1
#     return fac(n - 1) * n
#
# n = int(input('your number: '))
# print(fac(n))

# """

# """
# 'С помощью рекурсии выполните перевод числа в двоичную систему счисления'
# "10 - 1010"
# "12 - 1100"
# "3 - 11"
# "15 - 1111""
# l = []
# def convert(b):
#     if (b == 0):
#         return l
#     dig = b % 2
#     l.append(dig)
#     convert(b // 2)
# a = int(input("Введите число: "))
# convert(a)
# l.reverse()
# print("Двоичная форма числа:")
# for i in l:
#     print(i)
# """

# """
# 'Найдите длину списка при помощи рекурсии'
# a = [1, 2, 3, 'ab', 'token']
# def length(lst):
#     if not lst:
#         return 0
#     return 1 + length(lst[1:])
#
# print("Длина списка равна: ")
# print(length(a))
# """