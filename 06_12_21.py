# Task 1

from typing import List, Any

# def unique_list(elements: List[Any]) -> list:
#     return list(set(elements))    # It`s the best option.

def unique_list(elements: List[Any]) -> list:
    new_list = []
    for element in elements:
        if element not in new_list:
            new_list.append(element)
    return new_list


if __name__ == '__main__':
    print("Example:")
    print(unique_list([1, 1, 2, 3, 2, 5]))

    assert unique_list([1, 1, 1]) == [1]
    assert unique_list([1, 2, 1]) == [1, 2]
    assert unique_list(['a', 'a', 'a']) == ['a']
    assert unique_list(['a', 'b', 'b']) == ['a', 'b']
    assert unique_list([]) == []
    assert unique_list([1]) == [1]


# Task 2

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    new_list = [x for x in elements if x != elements[0]]
    if not new_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True

print("\n###\n")
# Task 3

def array_diff(a, b):
    while a:
        for i in a:
            if i in b:
                a.remove(i)
                b.remove(i)
            return a+b

def array_dif(a, b):
    for i in a:
        if i in b:
           return "yes"
        else:
            return "no"

a = [1, 2, 3]
b = [1, 2, 4]

print(array_dif(a, b))




def assert_equals(a, b, c):
    assert a == b, c


# if __name__ == '__main__':
#     assert_equals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
#     assert_equals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
#     assert_equals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
#     assert_equals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
#     assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
#     assert_equals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")


# Task 4

# def replace_last(line: list) -> list:
#     if not line:
#         return line
#     else:
#         new_list = [line[-1]]
#         new_list.extend(line[:-1])
#         return new_list

def replace_last(line: list) -> list:
    if not line:
        return line
    else:
        line[0:0] = [line[-1]]
        line.pop()
        return line

if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []


# Task 5

print(55555555)

from typing import Iterable


def except_zero(items: list) -> Iterable:
    if 0 in items:
        indexes_of_zero = [index for index in range(len(items)) if items[index] == 0]
        items.remove(0)
        items.sort()
        for i in indexes_of_zero:
            items.insert(i, 0)
            return items
    else:
        return items


print(list(except_zero([5, 3, 4, 1, 4, 7])))


# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    #assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    # assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    # assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    # assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    # assert list(except_zero([0, 0])) == [0, 0]

lst = [5, 3, 4, 1, 4, 7]
print(lst.sort())





