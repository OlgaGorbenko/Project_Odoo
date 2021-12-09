import collections



def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

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
    # print(first_list)

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