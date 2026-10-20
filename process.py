import os
import time
import multiprocessing


def show_process_info(label, delay=1):
    """Сообщает о запуске функции и выводит PID процесса."""
    print(f"[{label}] Функция запущена.")
    print(f"[{label}] PID процесса: {os.getpid()}")
    print(f"[{label}] PID родительского процесса: {os.getppid()}")
    time.sleep(delay)
    print(f"[{label}] Функция завершена.")


def first_task():
    print("\n=== Функция 1: информация о процессе ===")
    show_process_info("Функция 1", 1)


def second_task():
    print("\n=== Функция 2: ожидание ===")
    show_process_info("Функция 2", 2)


def third_task():
    print("\n=== Функция 3: отдельный процесс ===")
    show_process_info("Функция 3", 3)


def fourth_task():
    print("\n=== Функция 4: завершение ===")
    show_process_info("Функция 4", 1)


if __name__ == "__main__":
    print("Программа: процессы и потоки")
    print(f"PID главного процесса: {os.getpid()}")

    # Создаём четыре объекта Process для выполнения четырёх функций.
    process1 = multiprocessing.Process(target=first_task)
    process2 = multiprocessing.Process(target=second_task)
    process3 = multiprocessing.Process(target=third_task)
    process4 = multiprocessing.Process(target=fourth_task)

    processes = [process1, process2, process3, process4]

    # Запускаем процессы и выводим их ID.
    for process in processes:
        process.start()
        print(f"Запущен процесс с PID: {process.pid}")

    # Ждём завершения каждого процесса.
    for process in processes:
        process.join()
        print(f"Процесс с PID {process.pid} завершился. Код: {process.exitcode}")

    print("\nВсе процессы завершили работу.")
