# print("Lyubov Koroleva")
'''print("Я люблю учить Python!")
print("Привет, друг!, Как дела?")
print("Что нового в Python?")
print('Он сказал: "Привет!"')
print("It's his favourite language")
print("Python полезен; он интересен")
print("Я учу Python каждый день")
print("Первая строка")
print("Вторая строка")
print("Имя: Liubov \nВозраст: 74")
print("PYTHON ЭТО КРУТО".lower())
print("привет мир".upper())
print("Привет! Как дела? Все хорошо.")
print("Учить Python... это интересно...")
print("Я люблю Python")
print('"Я" "люблю" "Python"')
print("Python #1 @ school")
print("Привет!\nПривет, как дела?)
print("Hello", "123", "100")

name = "Liuba"
age = 30
print(name, age)
print("Hello", name)
print("How is it going?", name)
print("Bye", name)
print("123", 100, None, True)
print (10 // 3) # 3
print(10 % 3) # 1
print(10 ** 3)  # 1000 возведение в степень
print("1" + "23") # 123

x = 3
y = "5"
int_y = int(y) # "5" -> 5
str_x = str(x) # 3 -> "3"
print(x + int_y)

x = 100
y = 200
result = x + y
print(result)

print(1 + 1)
print(1 - 1)
print(5 * 2)
print(5 / 2)
print(10 // 3)
print(10 % 3)

message = input()
print(message)

a = input()
b = input()
print(a, b)
print(a + b)
int_a = int(a)
int_b = int(b)
print(int_a + int_b)

a = input("Введите первое число: ") # или a = int(input("Введите первое число: "))
b = input("Введите второе число: ")
print("Результат:", a + b)'''
from functools import total_ordering

from pyexpat.errors import messages

# message = "Привет"
# name = "Оксана"
# print(message + name)
# print(message + " " + name)
# print(message + ", " + name + "!")

# message = "Привет"
# name = "Оксана"
# age = 30
# result = f"{message}, {name}! Тебе {age} лет"
# result = message + ", " + name + "!" + " Тебе " + str(age) + " лет!" # Привет, Оксана! Тебе 30 лет!
# print(result)

# name = "Liubov"
# upper_name = name.upper()
# lower_name = name.lower()
# print(upper_name)
# print(lower_name)

# message = input("Enter a message: ") # или message = input().capitalize()
# print(message.capitalize())

# day = 28
# month = 10
# year = 1978
# info = "INFO Дата рождения пользователя: "
# print(info, day, "-", month, "-", year)
# print(info, end="")
# print(day, month, year, sep='-')
# print(info, f"{day} - {month} - {year}")

# text = "я программирую на Python каждый день\n"
# print(text.capitalize() * 10)

# name = input("Введите имя любимого человека: ")
# count_repeat = int(input("Введите число повторений: "))
# print((name.capitalize() + '\n') * count_repeat)

# # 14 * 3 + 2 : 20 - 17 * 16 + (126,9 + 103)
# a = 14 * 3 + 2 / 20 - 17 * 16 + (126.9 + 103)
# print(a)

# Сотрудники компании ScriptGalley Slaves могут получить следующую оплату в конце месяца:
# - оклад минус 20% оклада при эпик фейлах на проде
# - оклад при штатной работе
# - оклад + 5% оклада при успешном успехе.
# Напишите программу, которая получает на вход оклад сотрудника и выводит на печать все возможные варианты оплаты в конце месяца.

# salary = int(input("Введите свой оклад: "))
# salary_fail = salary * 0.8
# salary_success = salary * 1.05
# print(f"Оклад: {salary}, Эпик фейл: {salary_fail}, Успех: {salary_success}")

# (Для продвинутых и тех, кто любит математику) Пирожок в столовой стоит k рублей и m копеек. Какая сумма
# необходима для покупки N пирожков? Ответ выведите в рублях и копейках.
# Пример ввода 1:
# 10 (это рубли)
# 15 (копейки)
# 2 (число пирожков)
#
# Пример вывода 1:
# Сумма к оплате: 20 рублей 30 копеек.
# Пример ввода 2:
# 2
# 50
# 4
# Пример вывода 2:
# Сумма к оплате: 10 рублей 0 копеек.

k = int(input("Введите сумму за 1 пирожок к рублях: "))
m = int(input("Введите сумму за 1 пирожок в копейках: "))
n = int(input("Введите количество пирожков: "))

total_k = (k * 100 + m) * n

rub = total_k // 100
kop = total_k % 100

print(f"Сумма к оплате: {rub} руб. {kop} коп.")

