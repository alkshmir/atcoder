// dijkstraで最短距離とその時の経路を記録しておく
// 一回のdijkstraでO(N^2)でQ回あるのでO(QN^2)
// 最大で10^9位　あれ？間に合わんくね？

#include <bits/stdc++.h>
using namespace std;

void dijkstra(int s, vector<int>& dist, vector<vector<int> >& nodes, vector<int>& souvenir, vector<int> A){
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
    dist[s] = 0;
    //souvenir[s] = A[s];
    q.push(make_pair(0, s));
    while(!q.empty()){
        pair<int, int> p = q.top();
        q.pop();
        int v = p.second;
        if (nodes.empty() or nodes[v].empty()) continue;
        if (dist[v] < p.first) continue;
        for (int i = 0; i < nodes[v].size(); i++){
            int e = nodes[v][i];
            if (dist[e] > dist[v] + 1){
                dist[e] = dist[v] + 1;
                souvenir[e] = souvenir[v] + A[e];
                q.push(make_pair(dist[e], e));
            }
            if (dist[e] == dist[v] + 1){
                if (souvenir[e] < souvenir[v] + A[e]){
                    souvenir[e] = souvenir[v] + A[e];
                }
            }
        }
    }
}
int main(){
    int N;
    cin >> N;
    vector<vector<int> > dist(N, vector<int>(N, N+1)); // 都市から都市への距離
    vector<vector<int> > souvenir(N, vector<int>(N));
    vector<vector<int> > routes(N);
    vector<vector<int> > nodes(N); // 隣接リスト
    
    vector<int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i]; 
        souvenir[i][i] = 0;
    } 
    string s;
    for (int i = 0; i < N; i++){
        cin >> s;
        for (int j = 0; j < N; j++){
            if (s[j] == 'Y'){
                nodes[i].push_back(j);
                souvenir[i][j] = A[j];
            }
        }
    }
    /*
    for (int i = 0; i < N; i++){
        cout << "nodes[i].size() = " << nodes[i].size() << endl;
        for (int j = 0; j < nodes[i].size(); j++)
        cout << nodes[i][j] << endl;
    }
    */
    int Q, u, v;
    cin >> Q;
    for (int i = 0; i < Q; i++){
        cin >> u >> v;
        u--; 
        v--;
        dijkstra(u, dist[u], nodes, souvenir[u], A);
        if (dist[u][v] == N+1) cout << "Impossible" << endl;
        else cout << dist[u][v] << " " << souvenir[u][v] + A[u] << endl;
    }
    return 0;
}