N = int(input())
A = [int(s) for s in input().split()]

class Node(object):
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 
        self.parent = None

    def insert_left(self, value):
        if self.left == None:
            self.left = Node(value)
            self.left.parent = self
        else:
            t = Node(value)
            t.left = self.left
            self.left = t
            self.left.parent = self
        return self.left

    def insert_right(self, value):
        if self.right == None:
            self.right = Node(value)
            self.right.parent = self
        else:
            t = Node(value)
            t.right = self.right
            self.right = t
            self.right.parent = self
        return self.right

def generations(node: Node):
    cnt = 0
    def count(node: Node):
        nonlocal cnt
        if node.parent == None:
            return cnt
        else:
            cnt += 1
            return count(node.parent)
    count(node)
    return cnt

#bt = binarytree(1)
root = Node(1)
btree_dict = {1: root}
gens = {1:0}

for i, a in enumerate(A):
    i = i + 1
    #print(i, a)
    btree_dict[2*i] = btree_dict[a].insert_left(2*i)
    btree_dict[2*i+1] = btree_dict[a].insert_right(2*i+1)
    gens[2*i] = gens[a] + 1
    gens[2*i+1] = gens[a] + 1
for k in range(1, 2*N+2):
    #print(generations(btree_dict[k]))
    print(gens[k])