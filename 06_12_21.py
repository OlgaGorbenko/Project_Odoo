# # Даны стандартные размеры диванов
# #
# # Нужно найти наименьшее значение отклонения от стандартного размера
# #
# # For example:
# #
# # Product A = 150 cm
# # Product B = 160 cm
# # Product C = 170 cm
# #
# # Product Custom = 154 cm
# #
# #
# # Результат:
# # Custom cm = 4 cm
# #
#
#
# def get_custom_cm(custom_value):
#     standard_values = [180, 140, 160, 150, 170]
#     # new_value = custom_value - (custom_value//10)*10
#     if custom_value > standard_values[0]:
#         return abs(standard_values[0]-custom_value)
#     else:
#         new_value = round(custom_value, -1)
#         delt = abs(new_value - custom_value)
#         return delt
#
# print(get_custom_cm(187))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print('For custom value 137 =', get_custom_cm(137))
#
#     assert get_custom_cm(137) == 3
#     assert get_custom_cm(155) == 5
#     assert get_custom_cm(161) == 1
#     assert get_custom_cm(167) == 3
#     assert get_custom_cm(189) == 9
#     assert get_custom_cm(178) == 2




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
    list_numbers = [int(x) for x in list_numbers]
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


print(validate("4977949494949497"))

if __name__ == '__main__':
    print("Example:")
    print('4003600000000014 =', validate('4003600000000014'))

    assert validate('4003600000000014') is True
    assert validate('4400000000000008') is True
    assert validate('4000160000000004') is True
    assert validate('4977949494949497') is True






# ### Task 1 ###
#
# from typing import List, Any
#
# # def unique_list(elements: List[Any]) -> list:
# #     return list(set(elements))    # It`s the best option.
#
# def unique_list(elements: List[Any]) -> list:    # It`s another solution.
#     new_list = []
#     for element in elements:
#         if element not in new_list:
#             new_list.append(element)
#     return new_list
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(unique_list([1, 1, 2, 3, 2, 5]))
#
#     assert unique_list([1, 1, 1]) == [1]
#     assert unique_list([1, 2, 1]) == [1, 2]
#     assert unique_list(['a', 'a', 'a']) == ['a']
#     assert unique_list(['a', 'b', 'b']) == ['a', 'b']
#     assert unique_list([]) == []
#     assert unique_list([1]) == [1]
#
#
# ### Task 2 ###
#
# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     new_list = [x for x in elements if x != elements[0]]
#     if not new_list:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     assert all_the_same([1, 1, 1]) is True
#     assert all_the_same([1, 2, 1]) is False
#     assert all_the_same(['a', 'a', 'a']) is True
#     assert all_the_same([]) is True
#     assert all_the_same([1]) is True
#
#
# ### Task 3 ###
#
# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
# def assert_equals(a, b, c):
#     assert a == b, c
#
# if __name__ == '__main__':
#     assert_equals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
#     assert_equals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
#     assert_equals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
#     assert_equals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
#     assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
#     assert_equals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")
#
#
# ### Task 4 ###
#
# # def replace_last(line: list) -> list:    # Solution #1
# #     if not line:
# #         return line
# #     else:
# #         new_list = [line[-1]]
# #         new_list.extend(line[:-1])
# #         return new_list
#
# def replace_last(line: list) -> list:    # Solution #2
#     if not line:
#         return line
#     else:
#         line[0:0] = [line[-1]]
#         line.pop()
#         return line
#
# if __name__ == '__main__':
#     print("Example:")
#     print(replace_last([2, 3, 4, 1]))
#
#     assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
#     assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
#     assert replace_last([1]) == [1]
#     assert replace_last([]) == []
#
#
# ### Task 5 ###
#
# from typing import Iterable
#
#
# def except_zero(items: list) -> Iterable:
#     if 0 in items:
#         indexes_of_zero = [index for index in range(len(items)) if items[index] == 0]
#         items = sorted([x for x in items if x != 0])
#         while indexes_of_zero:
#             for index in indexes_of_zero:
#                 items.insert(index, 0)
#             indexes_of_zero.remove(index)    # в этои месте ругаеся на index, но код работает, тесты выполняются
#             return items
#     else:
#         return sorted(items)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
#
#     assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
#     assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
#     assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
#     assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
#     assert list(except_zero([0, 0])) == [0, 0]
#
#
#
