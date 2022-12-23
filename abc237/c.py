S = input()

start_a = 0
end_a = 0

for s in S:
    if s == 'a':
        start_a += 1
    else:
        break
for s in S[::-1]:
    if s == 'a':
        end_a += 1
    else:
        break
if end_a < start_a:
    print("No")
    exit()
# 末尾と最初のaを取り除いて回文かどうか調べる
if end_a:
    new_S = S[start_a:-end_a]
else:
    new_S = S[start_a:]
#print(new_S)
for i in range(len(new_S)//2):
    #print(i, new_S[i], new_S[-i-1])
    if new_S[i] != new_S[-i-1]:
        print("No")
        exit()
print("Yes")