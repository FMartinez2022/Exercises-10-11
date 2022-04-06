import string

cnt = 0
dct = dict()
dalst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            cnt += 1
            if letter not in dct:
                dct[letter] = 1
            else:
                dct[letter] += 1

for k, v in list(dct.items()):
    dalst.append((v / cnt, k))

dalst.sort(reverse=True)

for k, v in dalst:
    print(v, k)
