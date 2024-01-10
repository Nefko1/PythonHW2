"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
temperatur = [20, 25, 30, 35]
def temperature(temperatur):
    for temp in temperatur:
        print("Сейчас {} градусов".format(temp))
temperature(temperatur)
