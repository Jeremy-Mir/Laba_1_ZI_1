from random import randint

f_new = open('text.txt', 'r', encoding='utf-8')
new = input("Введите: ")
w = [["й","ц"],["у","к"],["е","н"],["г","ш"],["щ","з"],["х","ъ"]]
h = [["ф","ы"],["в","а"],["п","р"],["о","л"],["д","ж"],["э","я"]]
alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюябю.!,? "
mass = []

n = 0

for i in range(6):
    if n >= len(new):
        mass.append([])
    else:
        mass.append([])

    for j in range(6):
            if n >= len(new):
                mass[i].append(alf[0])
                alf = alf[1:]
            else:
                mass[i].append(new[n])
                alf = alf.replace(new[n], "", 1)
            n += 1
    print(*mass[i])

new = ""
for n in f_new.read() :
    for i in mass:
        a = 0
        for j in i:
            a = a + 1

            if j == n:
               # print(i.index(j),mass.index(i))
                if randint(0, 1) ==0:

                    new = new + w[i.index(j)][randint(0, 1)] + h[mass.index(i)][randint(0, 1)] + " "
                else:
                    new = new + h[mass.index(i)][randint(0, 1)] + w[i.index(j)][randint(0, 1)] + " "
print(new)


f_sif = open('text1.txt', 'w')
f_sif.write(new)
f_new.close()
f_sif.close()