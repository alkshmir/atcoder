#include <vector>
#include <iostream>
using namespace std;

void print(vector<vector<int> > v){
    for (int i = 0; i < v.size(); i++){
        cout << "[";
        for (int j = 0; j <v[i].size(); j++){
            cout << v[i][j];
            if (j != v[i].size() -1) cout << " ";
        }
        cout << "]";
        if (i != v.size() -1) cout << ", ";
    }
    cout << endl;
}
int main(){
    int N, X;
    cin >> N >> X;
    vector<vector<int> > dp(N+1, vector<int>(X+1, 0));
    vector<int> A(N), B(N);

    for (int i = 0; i <N; i++){
        cin >> A.at(i) >> B.at(i);
    }

    dp[0][0] = 1;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < X+1; j++){
            if (dp[i][j]){
                if (j+A[i] <= X) dp[i+1][j+A[i]] = 1;
                if (j+B[i] <= X) dp[i+1][j+B[i]] = 1;
            }
        }
    }
    //print(dp);
    if (dp[N][X]) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}