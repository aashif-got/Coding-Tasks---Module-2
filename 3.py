import random
n = 23
binary = bin(n)[2:]
print(f"binary equivalant of number is:{binary}" )
position = random.randint(0, len(binary) -1)
print(f"random position: {position}")
b = binary[-(position + 1)]
if b == '1':
    print("True (bit is 1)")
else:
    print("False (bit is 0)")


