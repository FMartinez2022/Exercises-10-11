dct = dict()
try:
    fhand = input('Enter File Name: ')
    namek = open(fhand)
except:
    print('File not found')
    quit()
for line in namek:
    words = line.split()
    if line.startswith('From ') :
        date = words [1]
        dct[date] = dct.get(date, 0) + 1

lst = list()
for k,v in dct.items() :
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v,k in lst[:1]:
    print(k,v)
