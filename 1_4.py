f_new = open('text.txt', 'r',encoding='windows-1251')
new = f_new.read()
n = 0
m = 31
okey = []
clkey = [2,3,6,13,27,52,105,210]
for i in clkey:
   n = n + i
n+=2

for i in clkey:
    okey.append((i*m)%n)
okey.reverse()
print("Open key = " )
print(okey)


f_sif = open('binar.bin', 'wb')
for s in new:
    bin = format(ord(s.encode('windows-1251')), 'b')[::-1]
    summ = 0
    n= 0
    print(bin)
    for b in bin:

        if b == '1':
           summ = summ + okey[n]
        n += 1
    print(summ)



    f_sif.write(summ.to_bytes(4,byteorder='big'))

f_new.close()
#