import time
from functools import wraps, reduce


def reverse_stroka(some_list): #1 task
    return str(some_list)


def value_more_then_ziro(some_list): #2 task
    return some_list > 0


def polindroms(some_list): #3 task
    if some_list == some_list[::-1]:
        return some_list


def timer(func): # 4 task создание декоратора
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        result_time = finish_time - start_time
        print(f"Выполнение функции polindroms заняло {result_time} секунд")
        return result
    return wrapper_timer


@timer #использование декоратора для задачи на полиндромность
def polindroms_two(some_list):
    return some_list == some_list[::-1]


def square_flat(length, width): #5 task
    return length * width


def option_menu():
    print("Возможные дальнейшие действия:"
          "\n'1' - Запустить задачу снова"
          "\n'2' - Выйти в главное меню"
          "\n'3' - Выйти из программы")

    choise_menu = input("Выбери действие:"
                        "\n")
    if choise_menu == '1':
        return 'repeat'
    elif choise_menu == '2':
        return 'menu'
    elif choise_menu == '3':
        exit()
    else:
        print("Что-то введено неверно")
        return 'menu'

while True:
    print(f"Домашняя работа Никитина Владислава"
      f"\n")
    print("Задача '1' - С помощью map() получить список, где каждое число из исходного списка переведено в строку"
             "\nЗадача '2' - С помощью filter() получить список тех элементов из исходного списка, значение которых больше 0"
             "\nЗадача '3' - С помощью filter() получить список тех строк из исходного списка, которые являются палиндромами"
             "\nЗадача '4' - Сделать декоратор, который измеряет время, затраченное на выполнение декорируемой функции"
             "\nЗадача '5' - Используя map() и reduce() посчитать площадь квартиры, имея на входе характеристики комнат квартиры"
             "\n'6' - Выход из программы")

    choise = input("Выберите интересующую вас задачу указав цифру соответствующую номеру:"
               "\n")


    if choise == '1':
        while True:
            print("Задача '1' - С помощью map() получить список, где каждое число из исходного списка переведено в строку")
            some_list = [1, 2, 3, 4, 5, 6, 7]
            print("Начальный список чисел:", some_list)
            result = list(map(reverse_stroka, some_list))
            print("Список, где каждое число - строка: ", result)
            result_program = option_menu()
            if result_program == 'menu':
                break
            elif result_program == 'repeat':
                continue


    elif choise == '2':
        while True:
            print("Задача '2' - С помощью filter() получить список тех элементов из исходного списка, значение которых больше 0")
            some_list = [-2, 5, -4, -87, 34, 12, 40]
            print("Начальный список чисел:", some_list)
            result = list(filter(value_more_then_ziro, some_list))
            print("Элементы больше 0:", result)
            result_program = option_menu()
            if result_program == 'menu':
                break
            elif result_program == 'repeat':
                continue


    elif choise == '3':
        while True:
            print("С помощью filter() получить список тех строк из исходного списка, которые являются палиндромами")
            some_list = ['шалаш', 'abba', 'ebde', '761286', 'see', 'bang_bang']
            print("Начальный список строк:", some_list)
            result = list(filter(polindroms, some_list))
            print("Строки полиндромы:", result)
            result_program = option_menu()
            if result_program == 'menu':
                break
            elif result_program == 'repeat':
                continue


    elif choise == '4':
        while True:
            print("Задача '4' - Сделать декоратор, который измеряет время, затраченное на выполнение декорируемой функции")
            print("Для решения задачи взят готовый декораотр подсчита времени и встроен в задачу '3'")

            some_list = ['шалаш', 'abba', 'ebde', '761286', 'see', 'bang_bang']
            print(f"Слова проверяемые на полиндромность, {some_list}")
            result = list(filter(polindroms_two, some_list))
            print(f"Слова полиндромы: {result}")
            result_program = option_menu()
            if result_program == 'menu':
                break
            elif result_program == 'repeat':
                continue


    elif choise  == '5':
        while True:
            print("Задача '5' - Используя map() и reduce() посчитать площадь квартиры, имея на входе характеристики комнат квартиры")

            rooms = [
        {"name": "Kitchen", "length": 9, "width": 8},
        {"name": "Room 1", "length": 12, "width": 13},
        {"name": "Room 2", "length": 3, "width": 2},
        {"name": "Room 3", "length": 7, "width": 12},
        {"name": "Room 4", "length": 11, "width": 7},
        {"name": "Room 5", "length": 5.3, "width": 8},
            ]
            print("В нашей просторной 5 комнатной квартире площадь каждой комнаты составляет: ", rooms)
            result_map = map(lambda x: x["length"] * x["width"], rooms)
            result_with_reduce = reduce(lambda y, x: x + y, result_map)

            print("Общая площадь квартиры", result_with_reduce)
            result_program = option_menu()
            if result_program == 'menu':
                break
            elif result_program == 'repeat':
                continue


    elif choise == '6':
        exit()

    else:
        print("Введена ерунда")












