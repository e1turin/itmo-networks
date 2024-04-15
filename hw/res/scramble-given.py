msg = 0xD2C8CD # encoded message
a = [int(i) for i in bin(msg)[2:]] 
# [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 
#  1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

b = [None for _ in a] # scrambled msg
c = [None for _ in a] # descrambled msg

# scramble
for i in range(len(a)):
    if i < 3:
        b[i] = a[i]
    elif i < 5:
        b[i] = a[i] ^ b[i-3] 
    else:
        b[i] = a[i] ^ b[i-3] ^ b[i-5]

# [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 
#  0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]

print(hex(int("".join(map(str,b)), 2))) # 0xcd00d1

# descramble
for i in range(len(a)):
    if i < 3:
        c[i] = b[i]
    elif i < 5:
        c[i] = b[i] ^ b[i-3] 
    else:
        c[i] = b[i] ^ b[i-3] ^ b[i-5]

print(all([a[i] == c[i] for i in range(len(a))])) # True



