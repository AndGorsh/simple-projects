"""проэкт"Таблица умножения".

Пользователь вводит число, которое будет перемножаться
на числа от 1 до 10.

"""


def i_x_m():
    for multiplier in range(1,11):
        print(i, "X", multiplier, "=", multiplier * i)

next_step = "да"

while next_step == "да":
    i = int(input("Для какого числа нужна таблица умножения? "))
    print("Вот ваша таблица:")

    i_x_m()
    print("Хотите еще?")
    next_step = input()
    if next_step != "да":
        print("К О Н Е Ц")


