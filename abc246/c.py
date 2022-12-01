N, K, X = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

sum_A = sum(A)
syou = [a // X for a in A]
amari = [a % X - X for a in A]
amari.sort(reverse=True)
son = [abs(a) for a in amari]
sum_syou = sum(syou)

#print(syou, amari, son)

if sum_syou >= K:
    print(sum(A)-K*X)
elif sum_syou + N >= K:
    print(sum(A)-K*X + sum(son[:K - sum_syou]) )
else:
    print(0)