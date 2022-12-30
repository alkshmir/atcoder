// 切ったら切ったところをリストに2分探索で突っ込んでいく。
// 木の長さを出力するクエリでは、xをリストで二分探索していれる場所を見つけ、
// その場所の両隣間の差を出力すれば良い
// C++ ではstd::setでできる
// 特に、c==2ではsetのlower_boundメソッドを使えば良い
#include <set>
#include <iostream>
using namespace std;
int main(){
    int L, Q;
    cin >> L >> Q;
    int c, x;
    int l, r;
    set<int> wood;
    for (int i = 0; i < Q; i++){
        cin >> c >> x;
        if (c==1){
            wood.insert(x);
        }else{
            auto itr = wood.lower_bound(x);
            if (itr==wood.begin()){
                l = 0;
            }else{
                l = *prev(itr);
            }
            if (itr==wood.end()){
                r = L;
            }else{
                r = *itr;
            }
            cout << r-l << endl;
        }
    }
    return 0;
}