# a = True
# b= False
# print(a, b)

# print(5 > 3)
# print(5 < 3)
# print(5 >= 3)
# print(5 <= 3)
# print(5 == 3)
# print(5 != 3)

# a = 1 > 2
# print(a)

# a = len("hello")
# print(a)
#
# result = len("hello") > 3
# print(result)

# a = "hello" == "Hello"
# print(a)
#
# a = "hello".lower() == "Hello".lower()
# print(a)

# print("abc" in "ABChelloabc")

# print("Hello".isdigit())
# print("Hello".isalpha())
# print("123".isdigit())

# print("Access denied")

# age = 26

# if age >= 18:
#     print("------")
#     print("You are old enough to go ahead")
#     print("------")
# else:
#     print("Access denied")

# age = 4
#
# if age <= 12:
#     print("Ребенок")
# elif age <= 17:
#     print("Подросток")
# else:
#     print("Взрослый")
#
# print("Continue")

# age = 20
# is_citizen = False
#
# if age >= 18 and is_citizen == True:
#     print("Welcome To The Citizen")
# else:
#     print("You cant be a citizen")

# age = 10
# is_student = False
# is_citizen = True
#
# if (age <= 18 or is_student == True) and is_citizen == True:
#     print("You get a discount")
#
# else:
#     print("You arent allowed to get a discount")

# a = 23
#
# if a:
#     print("a is true")

# a = 1, 45, -2 - 1, True, "abc", ...  # -> True
# b = 0, False, "", None, ... # -> False

# age = 19
# is_student = False
# is_citizen = True
#
# if (age <= 18 or is_student) and is_citizen:
#     print("You get a discount")
#
# else:
#     print("You arent allowed to get a discount")

# account = 50
#
# if account:
#     print(f"{account} on your account")
# else:
#     print("You dont have money on your account")

# for i in range(2):
#     print("------")
#     print("Hello World")
#     print("------")

# for letter in "APPLE":
#     print(letter)

# for i in range(3):
#     print("-----")
#     print(i)
#     print("-----")

# for letter in "APPLE":
#     print(f"Current letter {letter}")
#     if letter == "A":
#         print("Have found letter A!")

# number = range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# for i in number:
#     print(i)

# for i in number:
#     if i == 5:
#         print("Have found number 5!")

# number = range(10, 20)  # 10, 11, 12, ... 19
#
# for i in number:
#     print(i)

# counter = 0
#
# for letter in "APPLE":
#     print(f"Current letter {letter}")
#     if letter == "P":
#         print("Have found letter P!")
#         counter += 1
# print(counter)

# password = "12345!.5"

# for c in password:
#     print(c)
#     if c== ".":
#         print("have found banned symbol")
#         break
#
# print(password)

# message = "Hello! world!"
#
# цикл for повторяет код определенное количество раз

# for c in message:
#     if c == "!":
#         continue
#
#     print(c)

# password = "12345!.5"
#
# for c in password:
#     if c == ".":
#         continue
#     print(c)

# цикл while повторяет кусок кода ,пока выполняется определенное условие

# n = 10
#
# while n > 0:
#     print(n)
#
#     n = n - 1

# n = 10
#
# while n > 0:
#     print(n)
#     if n == 5:
#         break
#
#     n -= 1

# while True:
#     message = input("Enter a message: ")
#
#     print(message)
#
#     if message == "exit":
#         break

# review Olga
# задача а)
# x = 8
# y = 5
# z = 9
#
# if 0 < x <= 40 and y >= 10:
#     print("True")
# else:
#     print("False")

# задача б)
# x = 8
# y = 25
# z = 100
#
# if x + y > z or y + z > x:
#     print("True")
# else:
#     print("False")

# задача в)
# x = 8
# y = 25
# z = 100
#
# if x !=50 and z % y != 0:
#     print("True")
# else:
#     print("False")

# задача д)
# x = 8
# y = 25
# z = 100
#
# if not z < 356:
#     print("True")
# else:
#     print("False")

# 3. Напишите программу, которая определяет, состоит ли двузначное
# число, введенное с клавиатуры, из одинаковых цифр. Если состоит,
# то программа выводит «ДА», в противном случае программа
# выводит «НЕТ».

# num = int(input())
# if num > 10 and num + 5 < 0: # изначально невыполнимое условие
#     print("Вы победили")
# else:
#     print("Вы проиграли")

# x = int(input())
# if x in (11, 22, 33, 44, 55, 66, 77, 88, 99):
#     print("YES")
# else:
#     print("NO")

# x = int(input())
# if x // 10 == x % 10:
#     print("YES")
# else:
#     print("NO")

# x = (input())
# if x [0] == x [1]:
#     print("yes")
# else:
#     print("no")

# 4. При регистрации на сайтах требуется вводить пароль дважды.
# Это сделано для безопасности, поскольку такой подход уменьшает
# возможность неверного ввода пароля. Одновременно, пароль не
# должен быть меньше 8 символов. Напишите программу, которая сравнивает пароль и его
# подтверждение, а также проверяет длину пароля. Если они
# совпадают и пароль больше 8 символов, то программа выводит:
# «Пароль принят», иначе: «Пароль не принят» - если не совпадают
# или «Пароль слишком короткий».

# password = input("Enter your password: ")
# password2 = input("Enter your password again: ")
# if len(password) > 8:
#     if password == password2:
#         print("Password accepted")
#     else:
#         print("password is not accepted")
# else:
#     print("password too short")

# 5. Вам необходимо проанализировать введенное число 0 <= n <
# 1000, и вывести "Число однозначное", "Число двузначное" или
# "Число трехзначное" в зависимости от длины числа.

# n = input("Введите число от 1 до 1000 ")

# if 0 <= len(n) < 1000:
#     if len(n) == 1:
#         print("Число однозначное")
#     if len(n) == 2:
#         print("Число двузначное")
#     else:
#         print("Число трехзначное")

# n = int(input("Введите число от 1 до 999 "))
#
# if n < 10:
#     print("Число однозначное")
# if 10 <= n < 100:
#     print("Число двузначное")
# if n >= 1000:
#     print("число должно быть в пределах от 1 до 999")
# else:
#     print("Число трехзначное")

# 6. Стартапер Ваня продолжает разрабатывать свое приложение для
# влюбленных. Он решил создать рекомендательную систему для
# молодых людей с идеями, куда можно позвать девушку. Напишите
# программу, которая принимает на вход имя девушки и её увлечение
# и выводит идею вечернего досуга в виде фразы «“Имя“, пойдем
# “идея“.».
# Для имени Катя и увлечения «музыка»: «Катя, пойдем на концерт?»
# Для имени Катя и увлечения «спорт»: «Катя, пойдем в поход?»
# Для имени Катя и увлечения «театр»: «Катя, пойдем в театр?»
# Для всех остальных увлечений: «Катя, пойдем в ресторан?»

name = input("Enter her name: ")
interest = input("Enter her interest: ")
if name == "Katya" and interest == "music":
    print(f"{name}, пойдем на концерт?")
elif name == "Katya" and interest == "sport":
    print(f"{name}, пойдем в поход?")
elif name == "Katya" and interest == "theater":
    print(f"{name}, пойдем в театр?")
else:
    print(f"{name}, пойдем в ресторан?")

# 7. Напишите программу, принимающую на вход год и выводящую
# "Високосный", если в этом году действительно 366 дней, и
# "Невисокосный" иначе. Год считается високосным, если его номер
# делится на 4, но не делится на 100 или же делится на 400.

