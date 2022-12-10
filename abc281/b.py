import re
S = input()
if len(S) == 8 and re.match("[A-Z]", S[0]) and re.match("[A-Z]", S[-1]) \
    and re.match("[0-9].", S[1:-1]):
    try:
        n = int(S[1:-1])
    except:
        print("No")
        exit()
    if 100000 <= n < 999999:
        print("Yes")
        exit()
print("No")