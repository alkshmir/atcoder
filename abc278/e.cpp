#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    int H, W, N, h, w;
    cin >> H >> W >> N >> h >> w;

    vector<int> min_X(N, H + 1), max_X(N, 0), min_Y(N, W+1), max_Y(N, 0);
 
    int a;
    for(int i = 1; i <= H; ++i){
        for(int j=1; j<=W; ++j){
            cin >> a;
            a-=1;
            min_X[a] = min(min_X[a], i);
            max_X[a] = max(max_X[a], i);
            min_Y[a] = min(min_Y[a], j);
            max_Y[a] = max(max_Y[a], j);
        }
    }
    
    int cnt;
    for(int i=0; i <= H-h; ++i){
        for(int j=0; j <= W-w; ++j){
            int k = i+h, l = j+w;
            cnt = N;
            for(int a=0; a < N; ++a){
                if (i<min_X[a] && max_X[a]<=k && j<min_Y[a] && max_Y[a]<=l) cnt-=1;
            }
            //ans[k][l] = cnt;
            cout << cnt << " \n"[j == W - w];;
        }
    }
    return 0;
}