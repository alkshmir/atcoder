#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    int j;
    for(int i = 0; i<N; i++) cin >> A[i];
    int64_t ans = 0;
    vector<vector<int> > min_table(N, vector<int>(N, 1000 * 10000));
    for (int i = 0; i < N; i++){
        for (int j = i; j < N; j++){
            if (i==j) min_table[i][j] = A[i];
            else min_table[i][j] = min(min_table[i][j-1], A[j]);
            int64_t t = min_table[i][j]*(j-i+1);
            if (t > ans) ans = t;
        }
    }
    cout << ans << endl;
    return 0;
}