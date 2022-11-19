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