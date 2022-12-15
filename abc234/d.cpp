#include <vector>
#include <iostream>
#include <set>
using namespace std;

int main(){
    int N, K;
    cin >> N >> K;
    vector<int> P(N);
    for (int i = 0; i<N; i++) cin >> P.at(i);
    set<int> sub;
    for (int i = 0; i<K; i++){
        sub.insert(P[i]);
    }
    /*
    for(auto itr = sub.begin(); itr != sub.end(); ++itr) {
        cout << *itr << "\n";
    }
    */
    auto itr = sub.begin();

    for (int i = K; i < N; i++) {
        cout << *itr << endl;
        sub.insert(P[i]);
        if (P[i] > *itr) itr++;
    }
    cout << *itr << endl;
    return 0;
}