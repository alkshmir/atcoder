#include <set>
#include <queue>
#include <iostream>
using namespace std;

int main(){
    int Q, q, x;
    queue<int> que;
    multiset<int> s;
    cin >> Q;
    for (int i = 0; i<Q; i++) {
        cin >> q;
        if (q==1){
            cin >> x;
            que.push(x);
            //s.insert(x);
        }else if (q==2){
            if (!s.empty()){
                x = *s.begin();
                s.erase(s.find(x));
            } else {
                x = que.front();
                que.pop();
            }
            cout << x << endl;
        }else if (q==3){
            while(!que.empty()){
                s.insert(que.front());
                que.pop();
            }
        }
    }
    return 0;
}
