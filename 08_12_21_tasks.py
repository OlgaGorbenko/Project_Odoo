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
    # elif len(words_as_list) == 3 and ("".join(words_as_list)).isalpha():
    #     return True
    else:
        n = 0
        while n != len(words_as_list) - 2:
            new_list = ["".join(words_as_list[n:n + 3])]
            n += 1
            new_list.append("".join(words_as_list[n:n + 3]))

            return new_list, n

            # for i in new_list:
            #     if i.isalpha() in new_list:
            #         return True
            #     else:
            #         return False


# lst = ["cat", "5", "zet"]
#
# print("".join(lst[0:3]))


# print("hjkk2kvv".isalpha())

print(check("Hello World hello 2 new"))


# if __name__ == '__main__':
#     assert check("Hello World hello") is True, "Hello"
#     assert check("He is 123 man") is False, "123 man"
#     assert check("1 2 3 4 5") is False, "Digits"
#     assert check("bla bla bla bla") is True, "Bla Bla"
#     assert check("Hi") is False, "Hi"






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


print(sum_numbers('who is 1 1st 2 here'))


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


# def time_converter(time):
#     # replace this for solution
#     return time
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter('12:30 p.m.'))
#
#     assert time_converter('12:30 p.m.') == '12:30'
#     assert time_converter('9:00 a.m.') == '09:00'
#     assert time_converter('11:15 p.m.') == '23:15'