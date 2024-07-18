def personal_sum(numbers):  # возвращает кортеж из суммы чисел и кол-ва ошибок
    # создаю переменные для записи суммы чисел коллекции и записи неправильных данных (не числа)
    result = 0
    incorrect_data = 0
    # прохожу циклом по коллекции для сортировки на числа и неправильные данные
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):  # возвращает среднее арифметическое чисел коллекции
    try:
        # создаю список "num", в который передаются числа коллекции для определения
        # длины только числовых элементов, так как длина необходима для
        # получения среднего арифметического
        num = []
        for i in numbers:
            if isinstance(i, int or float):
                num.append(i)
            else:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
        # создаю переменную "summ", в которую закладывается первый элемент
        # возвращаемого кортежа первой функции (сумма всех чисел)
        summ = personal_sum(numbers)[0]
        average = summ / len(num)
        return average

    except ZeroDivisionError:  # выполняется, если передается не коллекция
        return 0
    except TypeError:  # выполняется, если передается число
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
