from pprint import pprint

# TODO решить с помощью list comprehension и распечатать его
spisok = [i for i in range(16)]

answer = []
for number in spisok:
    answer_number = {}
    answer_number['bin'] = answer_number.get("bin",bin(number))
    answer_number['dec'] = answer_number.get("dec", number)
    answer_number['hex'] = answer_number.get("hex", hex(number))
    answer_number['oct'] = answer_number.get("oct", oct(number))
    answer.append(answer_number)
pprint(answer)