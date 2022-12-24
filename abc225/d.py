class train():
    def __init__(self, id, left=None, right=None):
        self.id = id
        #if leader is not None:
        #    self.leader = leader
        #else:
        #    self.leader = id
        self.left = left
        self.right = right
    
def concat(train_x: train, train_y: train):
    train_y.right = train_x.id
    #train_y.leader = train_x.leader
    train_x.left = train_y.id

def separate(train_x: train, train_y: train):
    #train_y.leader = train_y.id
    train_y.right = None
    train_x.left = None

N, Q = [int(s) for s in input().split()]
query = []
for _ in range(Q):
    query.append([int(s) for s in input().split()])
trains = [train(i) for i in range(N)]

for q in query:
    if q[0] == 1:
        x = q[1]
        y = q[2]
        concat(trains[x-1], trains[y-1])
        #print(trains[x-1].leader, trains[x-1].left, trains[x-1].right)
    elif q[0] == 2:
        x = q[1]
        y = q[2]
        separate(trains[x-1], trains[y-1])
    elif q[0] == 3:
        x = q[1]
        # find leader
        t = trains[x-1]
        while t.right is not None:
            t = trains[t.right]

        tmp = [t.id]
        while t.left is not None:
            t = trains[t.left]
            tmp.append(t.id)
  
        print(' '.join([str(len(tmp))]+[str(n+1) for n in tmp]))