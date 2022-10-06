
f_new = open('text.txt', 'r',encoding='utf-8')
str = f_new.read()
gam = "KLUCH"
n = 0
c = []
fin = ""
for i in str:
    b = i.encode('windows-1251')
    a = gam[n].encode('windows-1251')
    c.append(ord(b) ^ ord(a))
    if n == 4:
        n=0
    else:
        n = n + 1
print(c)

for i in c:
    fin = fin + chr(i)

f_sif = open('text1.txt', 'w',encoding='utf-8')
f_sif.write(fin)
f_new.close()
f_sif.close()