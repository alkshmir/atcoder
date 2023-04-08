// 自分自身への閉路の最短距離
#include <bits/stdc++.h>
using namespace std;

void dijkstra(int s, vector<int>& dist, vector<vector<int> > nodes, bool flag){
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
    if (flag) {
        dist[s] = 0;
    }
    q.push(make_pair(dist[s], s));
    
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
                q.push(make_pair(dist[e], e));
            }
        }
    }
}

int main(){
    int N, Q;
    long long K, s, t;
    cin >> N >> K;
    vector<vector<int> > dist(N, vector<int>(N, N+1));
    vector<vector<int> > nodes(N);
    
    int tmp;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> tmp;
            if (tmp == 1) nodes[i].push_back(j); 
        }
    }
    cin >> Q;
    for (int i = 0; i < Q; i++){
        cin >> s >> t;
        if (s == t){
            cout << "0" << endl;
            continue;
        }
        int si = int((s-1) %N);
        int ti = int((t-1) %N);
        cout << si << ti << endl;
        bool flag = (si != ti);
        dijkstra(si, dist[si], nodes, flag);
        if (dist[si][ti] == N+1) cout << "-1" << endl;
        else cout << dist[si][ti] << endl;
    }
}