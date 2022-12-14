from collections import defaultdict
N = int(input())
S = input()

class doubly_linked_list(object):
    def __init__(self):
        self.nodes = defaultdict(lambda: [None, None])
        self.nodes[0] = [None, None]
        self.start = 0

    def insert_left(self, x, y):
        if self.nodes[x][0] == None:
            self.start = y
        else:
            t = self.nodes[x][0]
            self.nodes[t][1] = y
            self.nodes[y][0] = t
        self.nodes[x][0] = y
        self.nodes[y][1] = x

    def insert_right(self, x, y):
        if self.nodes[x][1] == None:
            pass
        else:
            t = self.nodes[x][1]
            self.nodes[t][0] = y
            self.nodes[y][1] = t
        self.nodes[x][1] = y
        self.nodes[y][0] = x

dll = doubly_linked_list()
for i, s in enumerate(S):
    if s == 'L':
        dll.insert_left(i, i+1)
    else:
        dll.insert_right(i, i+1)

#print(dll.nodes)
ans = []
n = dll.start
ans.append(str(n))
while dll.nodes[n][1] != None:
    #print(dll.nodes[n][1])
    n = dll.nodes[n][1]
    ans.append(str(n))
print(' '.join(ans))