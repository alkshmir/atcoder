# N個の円から2個選ぶ組み合わせそれぞれについて、接するかどうかを判定し、
# 接するならばUnion-Find木でuniteする。
# (sx, sy)と(tx, ty)についてそれぞれどの円周上の点なのかを判別する(O(N))
# その2つの円がUnion-Find木で同じrootを持っているならば、Yesを出力する。
# 従って、計算量O(N^2α(N))で判別することができる(α(N)はアッカーマン関数の逆数)
import itertools

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

# 2円が接するかどうかを返す
def sessuru(x1, y1, r1, x2, y2, r2):
    d = (x1-x2)**2 + (y1-y2)**2
    return (r1 - r2)**2 <= d <= (r1 + r2)**2


# 円周上の点かどうかを判別する
def onCircle(x, y, cx, cy, r):
    return (cx - x)**2 + (cy - y)**2 == r**2

N = int(input())
sx, sy, tx, ty = [int(s) for s in input().split()]
circles = []
for i in range(N):
    x, y, r = [int(s) for s in input().split()]
    circles.append((x, y, r, i))

uf = UnionFind(N)
for c1, c2 in itertools.combinations(circles, 2):
    if sessuru(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2]):
        uf.union(c1[3], c2[3])
    
#(sx, sy)と(tx, ty)についてそれぞれどの円周上の点なのかを判別する
for c in circles:
    if onCircle(sx, sy, c[0], c[1], c[2]):
        cs = c
    if onCircle(tx, ty, c[0], c[1], c[2]):
        ct = c

if uf.same_component(cs[3], ct[3]):
    print("Yes")
else:
    print("No")