import itertools

N, M = [int(s) for s in input().split()]

nums = list(range(1, M+1))
#print(nums)

for tup in list(itertools.combinations(nums, N)):
    print(' '.join([str(i) for i in tup]))


'''
for tup in list(itertools.product(nums, repeat=N)):
    flag = True
    for n in range(N-1):
        if tup[n] >= tup[n+1]:
            flag = False
            break
    if flag:
        #print(tup)
        
        print(' '.join([str(i) for i in tup]))
'''