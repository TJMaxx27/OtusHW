"""Модуль для вычисления средних значений."""


def calculate_average(input_nums):
    """ Вычисляем среднее значение списка чисел.
    В аргументах input_nums передаем список чисел.
    Возвращаем среднее значение float"""
    total = sum(input_nums)
    count = len(input_nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
