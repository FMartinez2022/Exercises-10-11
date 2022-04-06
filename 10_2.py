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
        hour = words[5]
        getit = hour.split(':')
        ope = getit[0]
        dct[ope] = dct.get(ope, 0) + 1

jk = (sorted([(k,v) for k,v in dct.items()]))
for v,k in jk :
    print(v,k)
