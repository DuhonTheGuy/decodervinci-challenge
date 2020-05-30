import string

letter_list1 = ['g', 'ha', 'o', 'od', 'l', 'vu', 'e', 'f', 'ck', 'u', 'n']
decoded = ''
number = 1
alphabet = string.ascii_lowercase

for i in letter_list1:
    print(str(i.count('d')) + str(i.count('e')) + str(i.count('c')) + str(i.count('o')) + str(i.count('d')) + str(i.count('r')) + str(i.count('v')))

# Output:
# 0000000
# 0000000
# 0001000
# 1001100
# 0000000
# 0000001
# 0100000
# 0000000
# 0010000
# 0000000
# 0000000

# for i in letter_list:
#     print(i
#     if i in alphabet:
#         a = alphabet.index(i
#         a += 1
#         decoded += alphabet[a]
# print(decoded


# print('10011110 10011000'.replace('1', 'd'.replace('0', 'b'.replace('d', '0'.replace('b', '1'
