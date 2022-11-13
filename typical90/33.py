H, W = [int(s) for s in input().split()]

if H==1 or W==1:
  ans = H*W
else:
  ans = ((H+1)//2) * ((W+1)//2)
print(ans)