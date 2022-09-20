from random import randint

f_naw = open('text.txt', 'r')
naw = "informaticsq"
w = [["q","w"],["e","r"],["t","y"],["u","i"],["o","p"],["a","s"]]
h = [["d","f"],["g","h"],["j","k"],["l","z"],["x","c"],["v","b"]]
alf = "abcdefghijklmnopqrstuvwxyz?!.-_,:; "
mass = []
print(len(naw))
n = 0

for i in range(6):
    if n >= len(naw):
        mass.append([])
    else:
        mass.append([])

    for j in range(6):
            if n >= len(naw):
                mass[i].append(alf[0])
                alf = alf[1:]
            else:
                mass[i].append(naw[n])
                alf = alf.replace(naw[n], "", 1)
            n += 1
    print(*mass[i])
naw = ""
for n in f_naw.read() :
    for i in mass:
        a = 0
        for j in i:
            a = a + 1
            if j == n:
                print(i.index(j),mass.index(i))
                naw = naw + w[i.index(j)][randint(0, 1)]  + h[mass.index(i)][randint(0, 1)] + " "
print(naw)


f_sif = open('text1.txt', 'w')
f_sif.write(naw)
f_naw.close()
f_sif.close()