sentence = 'Make a program that has some sentence on input' \
           ' and returns a dict containing all unique words ' \
           'as keys and the number of occurrences as values.'

sentence_list = sentence.split()
sentence_dict = {}
for word in sentence_list:
    sentence_dict[word] = len(word)

print(sentence_dict)


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total = {}
for s in stock:
    t = stock[s] * prices[s]
    total[s] = t

print(total)

i = [x for x in range(1, 11)]
j = [y**2 for y in i]
res = (i, j)
print(res)

rev_d = {v:k for k, v in total.items()}
print(rev_d)