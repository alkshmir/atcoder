Y = int(input())

amari = Y % 4
if amari == 2:
    print(Y)
elif amari == 1:
    print(Y+1)
elif amari == 0:
    print(Y+2)
elif amari == 3:
    print(Y+3)