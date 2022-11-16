N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
T = []
for _ in range(Q):
    T.append([int(s) for s in input().split()])

class series(object):
    def __init__(self):
        self.A = A
        self.shifts = 0

    def swap(self, x, y):
        tmp = self.A[(x-self.shifts)%N]
        self.A[(x-self.shifts)%N] = self.A[(y-self.shifts)%N]
        self.A[(y-self.shifts)%N] = tmp

    def shift(self):
        self.shifts += 1
    
    def print(self, x):
        print(self.A[(x-self.shifts)%N])

ser = series()

for t in T:
    x = t[1]
    y = t[2]
    if t[0] == 1:
        ser.swap(x-1, y-1)
    elif t[0] == 2:
        ser.shift()
    elif t[0] == 3:
        ser.print(x-1)