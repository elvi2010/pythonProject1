# #Теоритический вопрос №1
# #Ответ на вопрос
# #Переменная - это 'контейнер' со своим именем или ярлыком, в котором  хранятся некоторые данные определённого типа данных
# x = 12
#
# #Теоритический вопрос №2
# #Ответ на вопрос
# #Для хранения списка используется такой встроенный тип данных, как list или же коллекция
# list = [1, 2, 3, 3.14]
#
# #Теоритический вопрос №3
# #Ответ на вопрос
# #Цикл for - это конструкция в python, кторая позволяет повторять один и тот же блок кода заданное кол-во раз или для каждого элемента в заданной последовательности
# for i in range(5):
#     print(i)
#
# #Теоритический вопрос №4
# #Ответ на вопрос
# #Конструкция try-except нужна для обработки исключений то есть для того, чтобы программа не падала с ошибкой при возникновении непредвиденной ситуации, а корректно её обрабатывала.
# user_input = input("Введите число: ")
# try:
#     number = int(user_input)
#     print("Вы ввели число:", number)
# except ValueError:
#     print("Это не целое число, попробуйте ещё раз.")
#
# #Теоритический вопрос №5
# #Ответ на вопрос
# #В коде python если в коде будет деление на ноль, произойдёт ошибка ZeroDivisionError, и если его не обработать, программа аварийно завершится.
# a = 10
# b = 0
# result = a / b
# print("Это не выполнится")


# name=input("Введите ваше имя:")
# print("Привет,", name)
#
# user = (input("Введите целое число: "))
#
# try:
#     number = int(user)
#
#     if number % 2 == 0:
#         print(f"Число {number} — чётное.")
#     else:
#         print(f"Число {number} — нечётное.")
#
# except ValueError:
#     print("Это не целое число!")
#
# list = input("Введите список покупок: ")
#
# items = list.split(",")
#
#
# for item in items:
#  print(item.strip())
#
#  total = 0
#  count = 5
#
#  for i in range(1, count + 1):
#      while True:
#          user_input = input(f"Введите число #{i}: ")
#          try:
#              number = float(user_input)
#              total += number
#              break
#          except ValueError:
#              print("Это не число! Попробуйте ещё раз.")
#
#      print(f"Сумма всех чисел: {total}")
#      break

# user_input = input("Введите список чисел через запятую (например, 3, 5, -2, 10): ")
#
#
# parts = [p.strip() for p in user_input.split(',') if p.strip()]
#
# numbers = []
#
# for p in parts:
#     try:
#         num = float(p)
#         numbers.append(num)
#     except ValueError:
#         print(f"«{p}» не является числом — этот элемент будет пропущен.")
#
# if numbers:
#     max_number = max(numbers)
#
#     if max_number.is_integer():
#         max_number = int(max_number)
#     print(f"Самое большое число: {max_number}")
# else:
#     print("Не удалось получить ни одного корректного числа. Попробуйте снова.")

while True:
    password = input("Введите пароль: ")


    if len(password) < 6:
        print("Пароль слишком короткий. Попробуйте ещё раз.")
        continue


    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        print("Пароль должен иметь хотя бы одну цифру. Попробуйте ещё раз.")
        continue


    print("Пароль принят.")
    break












