#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    int64_t N, Q;
    cin >> N >> Q;
    vector<int64_t> T(Q), A(Q), B(Q);
    for (int64_t i = 0; i<Q; i++){
        cin >> T.at(i) >> A.at(i) >> B.at(i);
    }
    std::set<std::pair<int64_t, int64_t>> follows;

    for (int64_t i = 0; i<Q; i++){
        if (T[i] == 1){
            follows.insert(make_pair(A[i], B[i]));
        }else if (T[i] == 2){
            follows.erase(make_pair(A[i], B[i]));
        }else if (T[i] == 3){
            if (follows.count(make_pair(A[i], B[i])) && follows.count(make_pair(B[i], A[i]))){
                cout << "Yes" << endl;
            }else{
                cout << "No" << endl;
            }
        }
    }
    return 0;
}