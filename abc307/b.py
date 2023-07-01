# 50 * 49 = 2450この200文字の文字列に対して回文かどうか調べるので、十分間に合う
# 計算量はO(N|S_i|^2)
import itertools

def is_kaibun(a: str, b: str) -> bool:
    tmp = a + b
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[-1-i]:
            return False
    return True

N = int(input())
S = []
for _ in range(N):
    S.append(input())

for a, b in itertools.permutations(S, 2):
    if is_kaibun(a, b):
        print("Yes")
        #print(a, b)
        exit()
print("No")
