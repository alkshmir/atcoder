from collections import defaultdict
from typing import List
import sys
sys.setrecursionlimit(2000000)
class UnionFind:
    def __init__(self, n):
        # 要素数を記録する
        self.n = n
        # 各要素の親要素を示す配列を用意する
        # 要素のインデックスがその要素の親要素の番号を示す
        self.parent = [i for i in range(n)]
        # 各要素が属するグループのサイズを示す配列を用意する
        self.size = [1 for _ in range(n)]
        # 連結成分の個数を初期化する
        self.num_components = n

    # 要素xが属するグループを探す
    def find(self, x):
        # 要素xが属するグループの根を見つける
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        # 要素xから根までのパスをたどるときに、その間のすべての要素の親要素を根に繋ぎ変える
        # これを路径圧縮という
        while x != root:
            x, self.parent[x] = self.parent[x], root
        return root

    # 要素xが属するグループと要素yが属するグループを結合する
    def union(self, x, y):
        # 要素xが属するグループの根を探す
        x_root = self.find(x)
        # 要素yが属するグループの根を探す
        y_root = self.find(y)
        # 既に同じグループに属する場合は何もしない
        if x_root == y_root:
            return
        # グループのサイズが小さい方を大きい方に結合する
        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        # 連結成分の個数をカウントする
        self.num_components -= 1

    # グラフの連結成分の個数を求める
    def get_num_components(self):
        return self.num_components

    # 要素xが属するグループと要素yが属するグループが同じかどうかを判定する
    def same_component(self, x, y):
        return self.find(x) == self.find(y)

    # 異なる連結成分の根と含まれる頂点を列挙する関数
    def find_roots(self) -> List[int]:
        # 各頂点を探索する。
        roots = dict()
        for u in range(self.n):
            # uが属する集合の親を探す。
            p = uf.find(u)
            # 親が見つかったら、その親を根とする連結成分にuを追加する。
            if p in roots.keys():
                roots[p].append(u)
            else:
                roots[p] = [u]
        return roots

# 二部グラフ判定
def dfs(v) -> bool:
    visited[v] = True
    for dest in nxt[v]:
        if not visited[dest]:
            color[dest] = not color[v]
            if not dfs(dest):
                return False
        else:
            if color[dest] == color[v]:
                return False
    return True

N, M = [int(s) for s in input().split()]
node = defaultdict(list)

uf = UnionFind(N)
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    node[u].append(v)
    node[v].append(u)
    uf.union(u-1, v-1)

#print(node)

roots = uf.find_roots()
cnt = N*(N-1) // 2 - M
zero = False
# 各連結成分で二部グラフかどうかを確かめる
for root, subnodes in roots.items():

    nxt = defaultdict(list)
    for n in subnodes:
        for m in node[n+1]:
            nxt[n].append(m-1)
    #print(root, subnodes)

    # 各連結成分で、2色に塗られた頂点の数を求める(dfsで)
    visited = defaultdict(bool)
    color = dict()
    color[subnodes[0]] = True
    b = dfs(subnodes[0])
    # 二部グラフではない場合、答えは0
    if not b:
        zero = True
        break
    #print(color)
    # 黒に塗られている頂点の数
    black = 0
    white = 0
    for k, v in color.items():
        if v:
            black += 1
        else:
            white += 1
    cnt -= black*(black-1)//2
    cnt -= white*(white-1)//2

if zero:
    print(0)
else:
    print(cnt)
