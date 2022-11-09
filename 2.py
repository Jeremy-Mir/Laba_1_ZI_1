import os

f_new = open('new.bin', 'rb')
byt = f_new.read()
n = 0

k  = []

for i in range(0,8):
    k.append(os.urandom(4))
for l in k:

    print((l[0]))
h_b  = byt[:4]
l_b  = byt[-4:]
print("   ")

for n in range(0,4):
    print(byt[n])
  #  print(byt[n].to_bytes(1, byteorder="big"))
for n in range(0,4):



    k[0][n] = byt[n] | k[0][n]
print("   ")

for l in k:

    print((l))
f_new.close()