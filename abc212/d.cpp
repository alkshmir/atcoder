#include <set>
#include <iostream>
using namespace std;

int main(){
    int Q, P;
    long long x;
    multiset<long long> bag;
    unsigned long long offset = 0;
    cin >> Q;
    for (int i = 0; i < Q; i++){
        cin >> P;
        if (P == 1) {
            cin >> x;
            bag.insert(x-offset);
        }else if (P == 2){
            cin >> x;
            offset += x;
        }else if (P == 3){
            x = *bag.begin();
            cout << x + offset << endl;
            bag.erase(bag.begin());
        }
    }
    return 0;
}