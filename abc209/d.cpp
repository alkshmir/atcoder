// ciとdiの最短距離が偶数なら町で出会い、奇数なら道路で出会う
// 
#include <bits/stdc++.h>
using namespace std;

void dijkstra(int s, vector<int>& dist, vector<vector<int> >& nodes){
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
    dist[s] = 0;
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
                q.push(make_pair(dist[e], e));
            }
        }
    }
}
int main(){
    int N, Q, a, b, c, d;
    cin >> N >> Q;
    vector<vector<int> > dist(N, vector<int>(N, N));
    vector<vector<int> > nodes(N);
    for(int i = 0; i < N-1; i++){
        cin >> a >> b;
        nodes[a-1].push_back(b-1);
        nodes[b-1].push_back(a-1);
    }
    for(int i = 0; i < Q; i++){
        cin >> c >> d;
        c -= 1;
        d -= 1;
        int tmp_dist;
        if (dist[c][d] != N){
            tmp_dist = dist[c][d];
        }else if (dist[d][c] != N){
            tmp_dist = dist[d][c];
        }else{
            dijkstra(c, dist[c], nodes);
            tmp_dist = dist[c][d];
            //cout << dist[c][c] << endl;
        }
        if (tmp_dist % 2 == 0){
            cout << "Town" << endl;
        }else{
            cout << "Road" << endl;
        }
    }
    return 0;
}