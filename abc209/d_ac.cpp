#include <bits/stdc++.h>
using namespace std;

// 2部グラフの色分け
void dfs(int v, vector<bool>& visited, vector<bool>& color, vector<vector<int> >& nodes){
    visited[v] = true;
    if (nodes.empty() or nodes[v].empty()) return;
    for (int i = 0; i<nodes[v].size(); i++) {
        int e = nodes[v][i];
        if (visited[e]) continue;
        color[e] = !color[v];
        dfs(e, visited, color, nodes);
    }
}

int main(){
    int N, Q, a, b, c, d;
    cin >> N >> Q;
    vector<vector<int> > nodes(N);
    vector<bool> color(N);
    vector<bool> visited(N, false);
    for(int i = 0; i < N-1; i++){
        cin >> a >> b;
        nodes[a-1].push_back(b-1);
        nodes[b-1].push_back(a-1);
    }
    color[0] = true;
    visited[0] = true;
    dfs(0, visited, color, nodes);

    for (int i = 0; i < Q; i++){
        cin >> c >> d;
        c -= 1;
        d -= 1;
        if (color[c] == color[d]) cout << "Town" << endl;
        else cout << "Road" << endl;
    }

    return 0;
}