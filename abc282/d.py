from collections import defaultdict
import sys
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

    # 異なる連結成分の根を列挙する関数
    def find_roots(self) -> list[int]:
        # 各頂点を探索する。
        roots = set()
        for u in range(self.n):
            # uが属する集合の親を探す。
            p = uf.find(u)
            # 親が見つかったら、その親を根とする連結成分にuを追加する。
            roots.add(p)
        return roots

# 二部グラフ判定関数
def is_bipartite(uf: UnionFind, edges: list[tuple[int, int]]) -> bool:
    # 各辺を探索する。
    for u, v in edges:
        # uとvが同じ集合に属する場合は、このグラフは二部グラフではない。
        if uf.find(u) == uf.find(v):
            return False
        # uとvが異なる集合に属する場合は、uとvを同じ集合に結合する。
        else:
            uf.union(u, v)

    # 全ての辺を探索したら、終了する。このとき、グラフは二部グラフである。
    return True



N, M = [int(s) for s in input().split()]
node = defaultdict(list)
edges = []
uf = UnionFind(N)
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    node[u].append(v)
    node[v].append(u)
    edges.append((u-1, v-1))
    uf.union(u-1, v-1)

visited = defaultdict(bool)
color = dict()

roots = uf.find_roots()

for root in roots:
    
if len(roots) == 1:
    b = is_bipartite(N, edges)
    if b:
        print(N*(N-1)//2 - )
elif len(roots) == 2:
    pass
else:
    print(0)

