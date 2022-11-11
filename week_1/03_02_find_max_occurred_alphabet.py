input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrance = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrance = alphabet_occurrence_array[index]

        if alphabet_occurrance > max_occurrance:
            max_occurrance = alphabet_occurrance
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)


a = ['가','나','다']
# 3개의 공간을 사용..
b = 0
# 1개의 공간을 사용.