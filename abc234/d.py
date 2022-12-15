import bisect
N, K = [int(s) for s in input().split()]
P = [int(s) for s in input().split()]

class node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

table = [False for _ in range(N)]
for p in P[:K]:
    table[p-1] = True
sub = sorted(P[:K])
nodes = [None for _ in range(N)]
for i, s in enumerate(sub):
    nodes[s-1] = node(s)
    if i > 0:
        nodes[s-1].left = prev
        nodes[prev-1].right = s
    prev = s
ans = sub[::-1][K-1]
print(ans)
for i in range(K,N):
    
'''
for n in nodes:
    if n:
        print(n.value, n.left, n.right)
    else:
        print(n)
'''
