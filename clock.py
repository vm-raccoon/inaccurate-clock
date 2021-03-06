from datetime import datetime
import sys



def get_now():
    return datetime.now()


def datetime1():
    dict_prefix = {
        0: "",
        1: "Пятнадцать минут",
        2: "Половина",
        3: "Без четверти",
    }
    dict_postfix = {
        0: {
            0: "Двенадцать ночи",
            1: "первого ночи",
        },
        1: {
            0: "Час ночи",
            1: "второго ночи",
        },
        2: {
            0: "Два часа ночи",
            1: "третьего ночи",
        },
        3: {
            0: "Три часа ночи",
            1: "четвертого ночи",
        },
        4: {
            0: "Четыре часа ночи",
            1: "пятого утра",
        },
        5: {
            0: "Пять часов утра",
            1: "шестого утра",
        },
        6: {
            0: "Шесть часов утра",
            1: "седьмого утра",
        },
        7: {
            0: "Семь часов утра",
            1: "восьмого утра",
        },
        8: {
            0: "Восемь часов утра",
            1: "девятого утра",
        },
        9: {
            0: "Девять часов утра",
            1: "десятого утра",
        },
        10: {
            0: "Десять часов утра",
            1: "одинадцатого утра",
        },
        11: {
            0: "Одинадцать часов утра",
            1: "двенадцатого дня",
        },
        12: {
            0: "Двенадцать часов дня",
            1: "первого дня",
        },
        13: {
            0: "Час дня",
            1: "второго дня",
        },
        14: {
            0: "Два часа дня",
            1: "третьего дня",
        },
        15: {
            0: "Три часа дня",
            1: "четвертого дня",
        },
        16: {
            0: "Четыре часа дня",
            1: "пятого дня",
        },
        17: {
            0: "Пять часов дня",
            1: "шестого дня",
        },
        18: {
            0: "Шесть часов вечера",
            1: "седьмого вечера",
        },
        19: {
            0: "Семь часов вечера",
            1: "восьмого вечера",
        },
        20: {
            0: "Восемь часов вечера",
            1: "девятого вечера",
        },
        21: {
            0: "Девять часов вечера",
            1: "десятого ночи",
        },
        22: {
            0: "Десять часов ночи",
            1: "одинадцатого ночи",
        },
        23: {
            0: "Одинадцать часов ночи",
            1: "двенадцатого ночи",
        },
    }

    h = get_now().hour
    m = int(get_now().minute / 15)

    prefix = dict_prefix[m]

    if m == 0:
        postfix = dict_postfix[h][0]
    elif m in [1, 2]:
        postfix = dict_postfix[h][1]
    elif m == 3:
        if h == 23:
            h = 0
        postfix = dict_postfix[h][0]

    return prefix + ' ' + postfix


def datetime2():
    dict = {
        0: "Полночь",
        1: "Второй час ночи",
        2: "Третий час ночи",
        3: "Четвертый час ночи",
        4: "Пятый час утра",
        5: "Шестой час утра",
        6: "Седьмой час утра",
        7: "Восьмой час утра",
        8: "Девятый час утра",
        9: "Десятый час по полудню",
        10: "Одиннадцатый час по полудню",
        11: "Двенадцатый час по полудню",
        12: "Полдень",
        13: "Второй час после полудня",
        14: "Третий час после полудня",
        15: "Четвертый час дня",
        16: "Пятый час дня",
        17: "Шестой час вечера",
        18: "Седьмой час вечера",
        19: "Восьмой час вечера",
        20: "Девятый час вечера",
        21: "Десятый час ночи",
        22: "Одиннадцатый час ночи",
        23: "Двенадцатый час ночи",
    }
    return dict[get_now().hour]


def datetime3():
    h = get_now().hour
    txt = None
    if 5 <= h and h < 11:
        txt = "Утро"
    elif 10 <= h and h < 14:
        txt = "Полдень"
    elif 14 <= h and h < 19:
        txt = "День"
    elif 19 <= h and h < 22:
        txt = "Вечер"
    elif 22 <= h or h < 5:
        txt = "Ночь"
    return txt


def datetime4():
    w = get_now().weekday()
    txt = "Выходной!" if w in [5, 6] else "Рабочий день"
    return txt


def datetime5():
    w = get_now().weekday()
    h = get_now().hour
    txt = None
    if 6 <= h and h < 9:
        txt = "Пора вставать"
    elif 9 <= h and h < 10:
        txt = "По кофейку и работать!"
    elif 10 <= h and h < 12:
        txt = "Время работать"
    elif 12 <= h and h < 13:
        txt = "Обед, законный отдых"
    elif 13 <= h and h < 17:
        txt = "Работа, только работа"
    elif 17 <= h and h < 18:
        txt = "Работать до упора!"
    elif 18 <= h and h < 22:
        txt = "Время отдыха"
    elif 22 <= h or h < 6:
        txt = "Пора спать"
    return txt


accuracy = 1
if len(sys.argv) > 1:
    accuracy = int(sys.argv[1])
    if accuracy < 1 or accuracy > 5:
        accuracy = 1

method = "datetime" + str(accuracy)
text = None
if method in dir():
    text = globals()[method]()
print(text)
