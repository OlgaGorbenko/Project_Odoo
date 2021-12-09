# Task 1
# Вам дан список элементов.
# Нужно вернуть номер телефона в формате (888) 888-8888.
# Входные данные: Список.
# Выходные данные: Строка.

def create_phone_number(n) -> str:
    n = "".join(str(x) for x in n)
    n_1 = n[:3]
    n_2 = n[3:6]
    n_3 = n[6:]
    return f"({n_1}) {n_2}-{n_3}"


def assert_equals(a, b, c=''):
    assert a == b, c


if __name__ == '__main__':
    assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
    assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
    assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")



# Task 2
# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв.
# Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.

def check(words):
    words_as_list = words.split()
    if len(words_as_list) < 3:
        return False
    else:
        n = 0
        new_list = []
        while n != len(words_as_list) - 2:
            new_list.append("".join(words_as_list[n:n + 3]))
            n += 1
        if [x for x in new_list if x.isalpha()]:
            return True
        else:
            return False


if __name__ == '__main__':
    assert check("Hello World hello") is True, "Hello"
    assert check("He is 123 man") is False, "123 man"
    assert check("1 2 3 4 5") is False, "Digits"
    assert check("bla bla bla bla") is True, "Bla Bla"
    assert check("Hi") is False, "Hi"



# Task 3

import collections


def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    start_lst = list(text)

    idxs_of_extra_vowels = []
    for i, v in enumerate(start_lst):
        if v in consonants and v not in vowels:
            idxs_of_extra_vowels.append(i+1)

    for i in idxs_of_extra_vowels:
        start_lst[i] = ""

    first_list = []
    new_dict = dict(collections.Counter(start_lst))
    for x, y in new_dict.items():
        if y % 3 == 0:
            first_list.append(x)

    new_text = "".join(start_lst)

    while first_list:
        for i in first_list:
            if i in vowels and i*3 in new_text:
                new_text = new_text.replace(i*3, i)
        first_list.remove(i)

    return new_text


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"



# Task 4
# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.
# Текст состоит из чисел, пробелом и английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.

def sum_numbers(text: str) -> int:
    sum_of_numbers = 0
    text_as_list = text.split()
    for i in text_as_list:
        if i.isdigit():
            sum_of_numbers += int(i)
    return sum_of_numbers


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0



# Task 5

import datetime

def time_converter(time):
    if len(time) == 10:
        if "p" in time:
            if int(time[:2]) == 12:
                return time[:5]
            else:
                a = datetime.time(int(time[:2])+12, int(time[3:5]))
                return f"{a.hour}:{a.minute}"
    else:
        if "p" in time:
            a = datetime.time(int(time[:1]) + 12, int(time[2:4]))
            return f"{a.hour}:{a.minute}"
        else:
            a = datetime.time(int(time[:1]), int(time[2:4]))
            return str(a)[:5]


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'



# Task 6
# Класические крестики нолики
# Вам дан список с текстовыми значениями
# Нужно определить кто выиграл крестики или нолики
# Входные данные: Список.
# Выходные данные: Строка.

def check(game_result):
    if game_result[0][0] == game_result[0][1] == game_result[0][2]:
        return f"{game_result[0][0]}"
    if game_result[1][0] == game_result[1][1] == game_result[1][2]:
        return f"{game_result[1][0]}"
    if game_result[2][0] == game_result[2][1] == game_result[2][2]:
        return f"{game_result[2][0]}"

    if game_result[0][0] == game_result[1][0] == game_result[2][0]:
        return f"{game_result[0][0]}"
    if game_result[0][1] == game_result[1][1] == game_result[2][1]:
        return f"{game_result[0][1]}"
    if game_result[0][2] == game_result[1][2] == game_result[2][2]:
        return f"{game_result[0][2]}"

    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        return f"{game_result[0][0]}"
    if game_result[0][2] == game_result[1][1] == game_result[2][0]:
        return f"{game_result[0][2]}"

    else:
        return "D"


if __name__ == '__main__':
    assert check([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert check([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert check([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert check([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"