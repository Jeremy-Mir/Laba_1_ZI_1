import os

f_new = open('new.bin', 'rb')
byt = f_new.read()
n = 0

k  = []
S_block = [[4,10,9,2,13,8,0,14,6,11,1,12,7,15,5,3],[14,11,4,12,6,13,15,10,2,3,8,1,0,7,5,9],[5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11],[7,13,10,1,0,8,9,15,14,4,6,12,11,2,5,3],[],[],[],[]]
for i in range(0,8):
    k.append(os.urandom(4))
for l in k:

    print((l[0]))
h_b  = byt[:4]
l_b  = byt[-4:]
print("   ")
X = bytearray()
for n in range(0,4):
    print(byt[n])
print("   ")
  #  print(byt[n].to_bytes(1, byteorder="big"))



#for i in range(0,32):
for n in range(0,4):



    X.append((l_b[n] | k[0][n])%2**32)



f_new.close()