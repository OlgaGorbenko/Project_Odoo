import collections



def translate(text: str) -> str:
    new_string = text.replace(" ", "")
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    # for i in new_string:
    #     if i in consonants:
    #         new_string.replace(new_string)

    idxs_of_extra_vowels = []
    for i, v in enumerate(new_string):
        if v in consonants:
            idxs_of_extra_vowels.append(i+1)

    print(idxs_of_extra_vowels)

    for i in idxs_of_extra_vowels:
        new_string.replace(new_string[i], '')
    print(new_string)

print(translate("hieeelalaooo"))

    # first_list = []
    # second_list = []
    # new_dict = dict(collections.Counter(new_string))
    # for x, y in new_dict.items():
    #     if y % 3 == 0 or y % 4 == 0 or y % 5 == 0:
    #         first_list.append(x)
    #     if y < 3:
    #         second_list.append(x)
    # second_list = [x for x in second_list if x in vowels]
    # while first_list:
    #     for i in first_list:
    #         if i*4 in text:
    #             text = text.replace(i*4, i)
    #         else:
    #             text = text.replace(i*3, i)
    #     first_list.remove(i)
    # while second_list:
    #     for i in second_list:
    #         text = text.replace(i, "")
    #     second_list.remove(i)
    # return text


# if __name__ == "__main__":
#     print("Example:")
#     print(translate("hieeelalaooo"))
#
#     assert translate("hieeelalaooo") == "hello"
#     assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"     # how you duoin
#     assert translate("aaa bo cy da eee fe") == "a b c d e f"               # a b c da e fe
#     assert translate("sooooso aaaaaaaaa") == "sos aaa"                     # soso aaa