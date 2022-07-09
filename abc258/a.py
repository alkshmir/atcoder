K = int(input())
hours = int(K/60)
minutes = K%60
print('{:0>2d}:{:0>2d}'.format((21+hours)%24, minutes))