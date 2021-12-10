# Даны стандартные размеры диванов
#
# Нужно найти наименьшее значение отклонения от стандартного размера
#
# For example:
#
# Product A = 150 cm
# Product B = 160 cm
# Product C = 170 cm
#
# Product Custom = 154 cm
#
#
# Результат:
# Custom cm = 4 cm
#


def get_custom_cm(custom_value):
    standard_values = [180, 140, 160, 150, 170]
    if custom_value > standard_values[0]:
        return custom_value - standard_values[0]
    else:
        new_value = round(custom_value, -1)
        delt = abs(new_value - custom_value)
        return delt


if __name__ == '__main__':
    print("Example:")
    print('For custom value 137 =', get_custom_cm(137))

    assert get_custom_cm(137) == 3
    assert get_custom_cm(155) == 5
    assert get_custom_cm(161) == 1
    assert get_custom_cm(167) == 3
    assert get_custom_cm(189) == 9
    assert get_custom_cm(178) == 2

# Написать функцию проверки кредитных карт на валидность
#
# Пример:
#
# 4003600000000014
#
# Начиная с конца, каждую вторую цифру номера умножаем на 2 и складывем
# Если после умножения получается двухзначное число, то сумируем цифры этого числа
# 1*2 + 0*2 + 0*2 + 0*2 + 0*2 + 6*2 + 0*2 + 4*2
# 2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
# 2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
# Сумируем оставшиеся цифры с этой суммой
# 13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
# Если последняя цифра этой суммы равна нулю, то такая карта считается валидной
# 20 - последняя цифра 0 - эта карта валидна


def validate(card_number):
    list_numbers = list(card_number)
    list_numbers = [int(x) for x in list_numbers if x.isdigit()]
    new_list = [x*2 for x in list_numbers[::2]]
    tmp = []
    for i in new_list:
        if i >= 10:
            tmp.append(i)
    new_list_3 = [x for x in new_list if x < 10]
    sum_1 = sum(new_list_3)

    for ind, a in enumerate(tmp):
        x = [int(z) for z in str(a)]
        tmp[ind] = sum(x)
    sum_3 = sum(tmp)

    new_list_2 = [x for x in list_numbers[::-2]]
    sum_2 = sum(new_list_2)

    sum_all = sum_1 + sum_2 + sum_3
    lst = [int(z) for z in str(sum_all)]
    if lst[-1] == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print('4003600000000014 =', validate('4003600000000014'))

    assert validate('4003600000000014') is True
    assert validate('4400 0000 0000 0008') is True
    assert validate('4000 1600 0000 0004 ') is True
    assert validate('4977 9494 9494 9497') is True




# Данн размер препятствия n
# Нужно построить конструкцию такой формы и высотой n:
       #
      ##
     ###
    ####
   #####
  ######
 #######
########


import sys


def mario(n):
    symb_1 = "#"
    symb_2 = " "
    k = 1
    while k != n+1:
        print(symb_2*(n-k), symb_1*k)
        k += 1
    return


print(mario(8))


# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         n = int(sys.argv[1])
#     else:
#         n = 8
#     mario(n)


# Данн размер препятствия n
# Нужно вывести в консоль конструкцию такой формы и высотой n:
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########


import sys


def mario(n):
    symb_1 = "#"
    symb_2 = " "
    k = 1
    while k != n+1:
        print(symb_2*(n-k), symb_1*k, symb_1*k, symb_2*(n-k))
        k += 1
    return


print(mario(8))


# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         n = int(sys.argv[1])
#     else:
#         n = 8
#     mario(n)