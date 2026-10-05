# import time
#
# print("Управление машиной:")
# print("1 — запустить/продолжить движение")
# print("0 — остановить машину")
#
# start_time = None
#
# while True:
#     try:
#         command = int(input("Введите команду (1/0): "))
#     except ValueError:
#         print("Пожалуйста, введите целое число (1 или 0).")
#         continue
#
#     if command == 1:
#         if start_time is None:
#             start_time = time.time()
#             print("Машина запущена! Время движения: 0 секунд.")
#         else:
#             elapsed = time.time() - start_time
#             print(f"Машина едет... Прошло времени: {int(elapsed)} секунд.")
#
#     elif command == 0:
#         if start_time is not None:
#             elapsed = time.time() - start_time
#             print(f"\nМашина остановлена! Общее время движения: {int(elapsed)} секунд.")
#             start_time = None
#         else:
#             print("Машина ещё не была запущена.")
#
#
#     else:
#         print("Неверная команда. Используйте 1 для старта или 0 для остановки.")
#
#     time.sleep(0.1)


# nums = [1,2,3,4,5,6,7,8,9]
# print(nums)
# nums_squared = list(map(lambda x: x**2, nums))
# print(nums_squared)

# l =[22, 44, 333]
#
# def gen(l):
#     i = 0
#     while i < len(l):
#         yield l[i]
#         i += 1
#
# res = gen(l)
# print(next(res))
# print(next(res))
# print(next(res))
#
# res = map(float, l)
# print(next(res))
# print(next(res))
#
# def decor(func):
#     def wrapper():
#         print
#
# import random
# import time
#
# TASK_PULL = [
#     "Приобретать квартиру"
#     "Проверить трубы"
#     "Напугать жильцов"
#     "Покормить собаку"
# ]
# PLASES_PULL = [101,102,103,104,105]
# day = []
#
# def generate_day():
#     day = []
# place_pull = [PLASES_PULL[random.randint(0, len(PLASES_PULL)-1)] for i in range(random.randint(3,7))]
# for place in place_pull:
#     day.apenned({place: TASK_PULL[random.randint(0, len(TASK_PULL)-1)]})
# return day
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f'Время выполнения: {end_time - start}')
#         return result
#     return wrapper
#
#
# def print_day(day):
#     for task_and_place in day:
#         for place, task in task_and_place.items():
#             print(f'Задача: {task}, квартира: {place}')
# def start_day():
#     global day
#     if len(day) != 0:
#         print("День уже начал")
#         return
#     day = generate_day()
# def complete_task(place, task):
#     global day
#     if {int(place), task} in day:
#         print()
#         print(f'')




















#
# """set"""
# l = [22, 222, 22]
# st = set(l)
# print(st)
# st.add(100)
# print(st)
# print(st)
#
#
# """dict"""
#
# d = {'Valera': 'Not attention', 'Daniil': 'attention'}
# print(d['Valera'])
# print(d['Daniil'])
# print(d.keys())
# print(d.values())
# print(d.items())
#
# n = int(input('> '))
# for _ in range(n):
#     name, *marks = input('name marks: ').split()
#     marks = list(map(int, marks))
#     d[name] = round(sum(marks) / len(marks), 2)
#
# for nn, (k, v) in enumerate(d.items(), 1):
#     print(f'{nn}. {k}: {v}')

# class Animal():
#     def __init__(self,name):
#         self.name = name



