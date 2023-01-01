#include <set>
#include <iostream>
#include <vector>
using namespace std;

void dfs(int city, vector<set<int> >& nodes, vector<bool>& visited, vector<int>& journey){
    //journey.push_back(city);
    visited[city] = true;
    set<int> next = nodes[city];
    for (auto itr = next.begin(); itr != next.end(); itr++) {      
        if (visited[*itr]) continue;
        journey.push_back(city);
        dfs(*itr, nodes, visited, journey);
    }
    journey.push_back(city);
}

int main(){
    int N;
    int a, b;
    cin >> N;
    vector<set<int> > nodes(N);
    vector<bool> visited(N);
    vector<int> journey;
    for (int i = 0; i < N-1; i++) {
        cin >> a >> b;
        nodes[a-1].insert(b-1);
        nodes[b-1].insert(a-1);
    }
    dfs(0, nodes, visited, journey);
    for (int i=0; i<journey.size()-1; i++){
        cout << journey[i]+1 << " ";
    }
    cout << journey.back()+1 << endl;
    return 0;
}