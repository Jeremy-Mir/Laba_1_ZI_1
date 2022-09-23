f_new = open('text.txt', 'r',encoding='utf-8')
new = f_new.read()
fin = ""
n = int(input("Введите n: "))
for k in range(0,len(new)-1,n*4):
    for i in range(0,n):
        fin = fin + new[k + i]
        fin = fin + new[k + n+1+i*2]
        fin = fin + new[k + n * 3 + i]
        fin = fin + new[k + n+i*2]
print(fin)