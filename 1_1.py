from random import randint

f_naw = open('text.txt', 'r',encoding='utf-8')
naw = input("Введите: ")
w = [["й","ц"],["у","к"],["е","н"],["г","ш"],["щ","з"],["х","ъ"]]
h = [["ф","ы"],["в","а"],["п","р"],["о","л"],["д","ж"],["э","я"]]
alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюябю.!,? "
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
                if randint(0, 1) ==0:

                    naw = naw + w[i.index(j)][randint(0, 1)]  + h[mass.index(i)][randint(0, 1)] + " "
                else:
                    naw = naw + h[mass.index(i)][randint(0, 1)] + w[i.index(j)][randint(0, 1)]  + " "
print(naw)


f_sif = open('text1.txt', 'w')
f_sif.write(naw)
f_naw.close()
f_sif.close()