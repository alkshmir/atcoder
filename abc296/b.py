S = []
for _ in range(8):
    S.append(input())

d = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}
for i in range(8):
    for j in range(8):
        if S[-i-1][j] == "*":
            print(d[j] + str(i+1))
            exit()