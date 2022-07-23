N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))
#print(A)

correct = True

for i in range(N):
    for j in range(N):
        if i == j:
            break
        if (A[i][j] == 'W' and A[j][i] == 'L') or (A[i][j] == 'D' and A[j][i] == 'D') or (A[i][j] == 'L' and A[j][i] == 'W'):
            pass
        else:
            correct = False
            break 
    if not correct:
        break

if correct:
    print('correct')
else:
    print('incorrect')