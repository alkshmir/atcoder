#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M, a, b;
    cin >> N >> M;
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
    vector<int> dist(N, M);
    vector<long long> cnt(N, 0); // 各頂点から始点への最短経路数
    vector<vector<int> > nodes(N);
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        nodes[a-1].push_back(b-1);
        nodes[b-1].push_back(a-1);
    }

    
    // dijkstra ダイクストラ
    cnt[0] = 1;
    dist[0] = 0;
    q.push(make_pair(0, 0));
    while(!q.empty()){
        pair<int, int> p = q.top(); // distance, node index
        q.pop();
        int v = p.second;
        if (nodes.empty() or nodes[v].empty()) continue;
        if (dist[v] < p.first) continue;
        for (int i = 0; i < nodes[v].size(); i++){
            int e = nodes[v][i]; // edge
            if (dist[e] > dist[v] + 1){
                dist[e] = dist[v] + 1;
                cnt[e] = cnt[v];
                q.push(make_pair(dist[e], e));
            } else if (dist[e] == dist[v] + 1){
                cnt[e] += cnt[v];
                cnt[e] %= 1000000000 + 7;
            }
        }
    }
    cout << cnt[N-1] << endl;
    return 0;
}