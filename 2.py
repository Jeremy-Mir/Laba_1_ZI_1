import os
f_new = open('new.bin', 'rb')
byt = f_new.read()
n = 0

k  = []
S_block = [[4,10,9,2,13,8,0,14,6,11,1,12,7,15,5,3],
           [14,11,4,12,6,13,15,10,2,3,8,1,0,7,5,9],
           [5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11],
           [7,13,10,1,0,8,9,15,14,4,6,12,11,2,5,3],
           [6,12,7,1,5,15,13,8,4,10,9,14,0,3,11,2],
           [4,11,10,0,7,2,1,13,3,6,8,5,9,12,15,14],
           [13,11,4,1,3,15,5,9,0,10,14,7,6,8,2,12],
           [1,15,13,0,5,7,10,4,9,2,3,14,6,11,8,12]]
for i in range(0,8):
    k.append(os.urandom(4))
for l in k:

    print(l)
h_b  = byt[:4]
l_b  = byt[-4:]
print("   ")
X = bytearray()
S = bytearray()
Z = bytearray()
for n in range(0,4):
    print(byt[n])
print("   ")
  #  print(byt[n].to_bytes(1, byteorder="big"))



for i in range(0,32):
    X.clear()
    S.clear()
    Y = 0
    Z.clear()
    if i <24:
        ki = i % 8
    else:
        ki = 7 - (i % 8)
   # print("   ")
    for n in range(0,4):

        X.append((l_b[n] | k[ki][n])%2**32)

  #  print("X = ")
    #for l in X:
    #    print(l)

    # if len(bin(X[3]).lstrip('0b'))<8:
    #      print("0"+bin(X[3]).lstrip('0b'))
    # else:

    # print(int(bin(X[0]).lstrip('0b')[:4],2) )
    # print(int(bin(X[0]).lstrip('0b')[4:],2) )
    # print(int(bin(X[1]).lstrip('0b')[:4],2) )
    # print(int(bin(X[1]).lstrip('0b')[4:],2) )
    #  print(int(bin(X[2]).lstrip('0b')[:4],2) )
    #  print(int(bin(X[2]).lstrip('0b')[4:],2) )
    # # print(int(("0"+bin(X[3]).lstrip('0b'))[:4],2) )
    # # print(int(("0"+bin(X[3]).lstrip('0b'))[4:],2) )
    # #print(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4],2)]).lstrip('0b')+"0000",2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:],2) ]).lstrip('0b'),2))







    if len(bin(X[0]).lstrip('0b'))<8:

        if int(bin(X[0]).lstrip('0b')[4:], 2) != 13:
            S.append(int(bin(S_block[0][int("0"+bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[0][int("0"+bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    else:

        if int(bin(X[0]).lstrip('0b')[4:], 2) != 13:
            S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    if len(bin(X[1]).lstrip('0b'))<8:

        if int(bin(X[1]).lstrip('0b')[4:], 2) != 4:
            S.append(int(bin(S_block[2][int("0"+bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[3][int(bin(X[1]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[2][int("0"+bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    else:

        if int(bin(X[1]).lstrip('0b')[4:], 2) != 4:
            S.append(int(bin(S_block[2][int(bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[3][int(bin(X[1]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[2][int(bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    if len(bin(X[2]).lstrip('0b'))<8:

        if int(bin(X[2]).lstrip('0b')[4:], 2) != 3:
            S.append(int(bin(S_block[4][int("0"+bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[5][int(bin(X[2]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[4][int("0"+bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    else:

        if int(bin(X[2]).lstrip('0b')[4:], 2) != 3:
            S.append(int(bin(S_block[4][int(bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[5][int(bin(X[2]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[4][int(bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    if len(bin(X[3]).lstrip('0b'))<8:

         if int(bin(X[3]).lstrip('0b')[4:], 2) != 3:
             S.append(int(bin(S_block[6][int("0"+bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[7][int("0"+bin(X[3]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
         else:
             S.append(int(bin(S_block[6][int("0"+bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    else:


        if int(bin(X[3]).lstrip('0b')[4:], 2) != 3:
            S.append(int(bin(S_block[6][int(bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(bin(S_block[7][int(bin(X[3]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
        else:
            S.append(int(bin(S_block[6][int(bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

    #S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4],2)]).lstrip('0b')+"0000",2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:],2) ]).lstrip('0b'),2))

   # print("  ")
   # print("S = ")
   # for l in S:

       # print(l)
    Y = bin(int.from_bytes(S, 'big')).lstrip('0b')
    if len(Y) < 32:
        for i in range(0,32-len(Y)):
            Y = "0" + Y

    Y = Y[11:]+Y[:11]

  #  print("  ")
  #  print("Y = ")
   # print(Y)


    Z.append(int(Y[:8],2))
    Z.append(int(Y[8:16], 2))
    Z.append(int(Y[16:24], 2))
    Z.append(int(Y[24:32], 2))
  #  print("Z = ")
  #  for l in Z:

    #    print(l)

    Z[0] = h_b[0]^Z[0]
    Z[1] = h_b[1]^Z[1]
    Z[2] = h_b[2]^Z[2]
    Z[3] = h_b[3]^Z[3]
   # print("h_b = ")
    #for l in Z:

      #  print(l)
    if i < 32:
        temp_b = h_b
        h_b = l_b
        l_b = temp_b


###############################################
fin_b = l_b + h_b
h_b  = fin_b[:4]
l_b  = fin_b[-4:]
for l in fin_b:
    print("l =",l)
print("  ")
for i in range(0, 32):
        X.clear()
        S.clear()
        Y = 0
        Z.clear()
        if i < 8:
            ki = i % 8
        else:
            ki = 7 - (i % 8)
        #print("   ")
        for n in range(0, 4):
            X.append((l_b[n] | k[ki][n]) % 2 ** 32)

        #print("X = ")
      #  for l in X:
           # print(l)

        # if len(bin(X[3]).lstrip('0b'))<8:
        #      print("0"+bin(X[3]).lstrip('0b'))
        # else:

        # print(int(bin(X[0]).lstrip('0b')[:4],2) )
        # print(int(bin(X[0]).lstrip('0b')[4:],2) )
        # print(int(bin(X[1]).lstrip('0b')[:4],2) )
        # print(int(bin(X[1]).lstrip('0b')[4:],2) )
        #  print(int(bin(X[2]).lstrip('0b')[:4],2) )
        #  print(int(bin(X[2]).lstrip('0b')[4:],2) )
        # # print(int(("0"+bin(X[3]).lstrip('0b'))[:4],2) )
        # # print(int(("0"+bin(X[3]).lstrip('0b'))[4:],2) )
        # #print(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4],2)]).lstrip('0b')+"0000",2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:],2) ]).lstrip('0b'),2))

        if len(bin(X[0]).lstrip('0b')) < 8:

            if int(bin(X[0]).lstrip('0b')[4:], 2) != 13:
                S.append(int(bin(S_block[0][int("0" + bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[0][int("0" + bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        else:

            if int(bin(X[0]).lstrip('0b')[4:], 2) != 13:
                S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        if len(bin(X[1]).lstrip('0b')) < 8:

            if int(bin(X[1]).lstrip('0b')[4:], 2) != 4:
                S.append(int(bin(S_block[2][int("0" + bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[3][int(bin(X[1]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[2][int("0" + bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        else:

            if int(bin(X[1]).lstrip('0b')[4:], 2) != 4:
                S.append(int(bin(S_block[2][int(bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[3][int(bin(X[1]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[2][int(bin(X[1]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        if len(bin(X[2]).lstrip('0b')) < 8:

            if int(bin(X[2]).lstrip('0b')[4:], 2) != 3:
                S.append(int(bin(S_block[4][int("0" + bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[5][int(bin(X[2]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[4][int("0" + bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        else:

            if int(bin(X[2]).lstrip('0b')[4:], 2) != 3:
                S.append(int(bin(S_block[4][int(bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[5][int(bin(X[2]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[4][int(bin(X[2]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        if len(bin(X[3]).lstrip('0b')) < 8:

            if int(bin(X[3]).lstrip('0b')[4:], 2) != 3:
                S.append(int(bin(S_block[6][int("0" + bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[7][int("0" + bin(X[3]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[6][int("0" + bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        else:

            if int(bin(X[3]).lstrip('0b')[4:], 2) != 3:
                S.append(int(bin(S_block[6][int(bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2) | int(
                    bin(S_block[7][int(bin(X[3]).lstrip('0b')[4:], 2)]).lstrip('0b'), 2))
            else:
                S.append(int(bin(S_block[6][int(bin(X[3]).lstrip('0b')[:4], 2)]).lstrip('0b') + "0000", 2))

        # S.append(int(bin(S_block[0][int(bin(X[0]).lstrip('0b')[:4],2)]).lstrip('0b')+"0000",2) | int(bin(S_block[1][int(bin(X[0]).lstrip('0b')[4:],2) ]).lstrip('0b'),2))

       # print("  ")
       # print("S = ")
        #for l in S:
         #   print(l)
        Y = bin(int.from_bytes(S, 'big')).lstrip('0b')
        if len(Y) < 32:
            for i in range(0, 32 - len(Y)):
                Y = "0" + Y

        Y = Y[11:] + Y[:11]

      #  print("  ")
       # print("Y = ")
      #  print(Y)

        Z.append(int(Y[:8], 2))
        Z.append(int(Y[8:16], 2))
        Z.append(int(Y[16:24], 2))
        Z.append(int(Y[24:32], 2))
       # print("Z = ")
        #for l in Z:
        #    print(l)

        Z[0] = h_b[0] ^ Z[0]
        Z[1] = h_b[1] ^ Z[1]
        Z[2] = h_b[2] ^ Z[2]
        Z[3] = h_b[3] ^ Z[3]
     #   print("h_b = ")
     #   for l in Z:
      #      print(l)
        if i < 32:
            temp_b = h_b
            h_b = l_b
            l_b = temp_b

fin_b = l_b + h_b
for l in fin_b:
    print("l =",l)
f_new.close()