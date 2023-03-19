#include <iostream>
#include <set>
using namespace std;

int main(){
    int N, Q;
    cin >> N >> Q;
    int e, x;
    set<int> not_called;
    set<int> called;
    set<int> done;
    for(int i=0; i < N; i++){
        not_called.insert(i+1);
    }
    for (int i = 0; i < Q; i++){
        cin >> e;
        if (e == 2){
            cin >> x;
        }
        if (e == 1){
            auto itr = not_called.begin();
            called.insert(*itr);
            not_called.erase(*itr);
        }else if (e == 2){
            done.insert(x);
            called.erase(x);
        }else{
            auto itr = called.begin();
            cout << *itr << endl;
        }
    }
    return 0;
}