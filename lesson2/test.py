# kio = "dfgh     sdfgdfg dfgfgdf    dfgdfg"
# print(kio.replace('\n', ''))
#
# import re
#
# print(re.sub(r'\s{2,}', ' ', kio))

# row = ['Имя узла:                         Comp1']
#
# myString = ';'.join(row)
# print(type(myString))
# print(myString)

import re

with open('info_1.txt') as f_n:
    arr = []
    for row in f_n:
        # myString = ';'.join(row)
        # new_row = re.sub(r'\s{2,}', ' ', myString)
        # print(new_row)
        new_row = re.sub(r'\s{2,}', ' ', row)
        # print(new_row)
        arr.append(new_row)
    print(arr)
    # myString = ';'.join(arr)