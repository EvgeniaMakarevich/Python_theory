# import json
# import pytest
#
# dct = {
#     'hello' : 'world'
# }
#
# file_name = 'new_file.json'
# with open(file_name, 'w') as f:
#     json.dump(dct, f)
#
#
# with open(file_name, 'r') as f:
#     a = json.load(f)
#
#
# print(a)
#
# @pytest.mark.slow
# def test_calc():
#     a = 4
#     b = 5
#     assert a + b  == 9
#
#
# def test_2():
#     assert 0 == 0
#
#

def first_last(letter, st):
    l = []
    if not letter in st:
        return (None,None)
    else:
        for index, symbol in enumerate(st):
            if symbol == letter:
                l.append(index)

    return(l[0], l[-1])

print(first_last('a', 'ananas'))

