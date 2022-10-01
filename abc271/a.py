N = int(input())

if N <= 15:
    print('0' + hex(N)[2:].upper())
else:
    print(hex(N)[2:].upper())