# abc278 感想

## c問題
https://atcoder.jp/contests/abc278/tasks/abc278_c

マジ悔しい。
はじめ各ユーザごとにfolloweeを管理するsetを持つ方針で進めたが、pythonで提出するとTLE。
```python
N, Q = [int(s) for s in input().split()]
T = []
A = []
B = []
for _ in range(Q):
    t, a, b = [int(s) for s in input().split()]
    T.append(t)
    A.append(a)
    B.append(b)

follows = [set() for _ in range(N+1)]

for t, a, b in zip(T, A, B):
    if t == 1:
        follows[a].add(b)
    elif t == 2:
        follows[a].discard(b)
    elif t == 3:
        if b in follows[a] and a in follows[b]:
            print("Yes")
        else:
            print("No")
```
pythonが遅いのかと思って、C++で書き直したら、RE
```cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    int64_t N, Q;
    cin >> N >> Q;
    vector<int64_t> T(Q+1), A(Q+1), B(Q+1);
    for (int64_t i = 0; i<Q; i++){
        cin >> T.at(i) >> A.at(i) >> B.at(i);
    }
    vector<std::set<int64_t>> follows(N+2);

    for (int64_t i = 0; i<Q; i++){
        if (T[i] == 1){
            follows[A[i]-1].insert(B[i]-1);
        }else if (T[i] == 2){
            follows[A[i]-1].erase(B[i]-1);
        }else if (T[i] == 3){
            if (follows[A[i]-1].count(B[i]-1) && follows[B[i]-1].count(A[i]-1)){
                cout << "Yes" << endl;
            }else{
                cout << "No" << endl;
            }
        }
    }
    return 0;
}
```
こういうテストケースでエラーが出た
```
1000000000 3
1 2 3
2 3 2
3 2 3
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```
C++よく知らないので何が起こってるのかわからなかったが、メモリを確保できないときにこういうエラーが出るらしい。
なぜメモリを確保できないのかわからなかったが、解説読んでようやく気付いた。

問題は、N=10^9程度のときに、10^9人のユーザそれぞれに対して(かなり少なく見積もって)8byteなりのデータを管理すると、
少なくとも8GBはメモリが必要になることである。
1ユーザあたり8byteとしているのは`int64_t`1つ分の話で、実際はその何倍も必要であろう(std::set1つ分がどれぐらいメモリを使うのか知りませんが)。

pythonでは、10^9個のsetを動的に確保するところで非常に時間がかかっていたのではないかと予想(計測してないので、あくまで予想)。
- というか、他の部分が$O(Q)$だったとしても`follows = [set() for _ in range(N+1)]`が既に$O(N)$ですね。アホすぎる…

MLEが出ていればメモリが足りないのかな？というあたりは付けられたのですが、TLEやREだったので原因がわかりませんでした…

というわけでメモリをアホほど使う解法では、MLEではなくてTLEやREが出ることもあるという教訓でした。
変数の初期化にかかる計算量も意識できれば、誤った解法なことがわかったはずなので反省。

## 正答
[解説](https://atcoder.jp/contests/abc278/editorial/5230)にも書いてありますが、全ユーザーのfollow状況を管理するsetを1つ用意すれば解けます。
```python
N, Q = [int(s) for s in input().split()]
T = []
A = []
B = []
for _ in range(Q):
    t, a, b = [int(s) for s in input().split()]
    T.append(t)
    A.append(a)
    B.append(b)

#follows = [set() for _ in range(N+1)]
follows = set()

for t, a, b in zip(T, A, B):
    if t == 1:
        follows.add((a, b))
    elif t == 2:
        follows.discard((a, b))
    elif t == 3:
        if (a, b) in follows and (b, a) in follows:
            print("Yes")
        else:
            print("No")
```