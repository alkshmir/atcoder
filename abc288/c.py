
# Union-Findを実装するクラス
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

N, M = [int(s) for s in input().split()]
#nodes = defaultdict(list)
uf = UnionFind(N+1)
cnt = 0
for _ in range(M):
    a, b = [int(s) for s in input().split()]
    #nodes[a].append(b)
    #nodes[b].append(a)
    if uf.same_component(a, b):
        cnt += 1
    uf.union(a, b)

print(cnt)