str = ")9/'k;:/,"
gam = "KLUCH"
n = 0
c = []
fin = ""
for i in str:
    b = i.encode('windows-1251')
    a = gam[n].encode('windows-1251')
    c.append(ord(b) ^ ord(a))
    print(c)
    if n == 4:
        n=0
    else:
        n = n + 1
for i in c:
    fin = fin + chr(i)
print(fin)