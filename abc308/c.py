
class success_rate(object):
    def __init__(self, a, b, idx):
        self.a = a
        self.b = b
        self.idx = idx

    def __lt__(self, other):
        if self.a * (other.a + other.b) == other.a * (self.a + self.b):
            return self.idx < other.idx
        return self.a * (other.a + other.b) > other.a * (self.a + self.b)

N = int(input())
sr = []
for i in range(N):
    a, b = [int(s) for s in input().split()]
    sr.append(success_rate(a, b, i))

print(' '.join([str(s.idx+1) for s in sorted(sr)]))
#print(' '.join([str(i+1) for i in idx]))