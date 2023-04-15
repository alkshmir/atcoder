#include <iostream>
#include <set>
#include <vector>
#include <map>

using namespace std;
int main(){
    int N, Q, n, i, j;
    cin >> N >> Q;
    map<int, multiset<int> > card_in_hako; // ハコに入っているカード
    map<int, set<int> > hako_with_card;


    for (int q = 0; q < Q; q++){
        cin >> n >> i;
        if (n == 1) {
            cin >> j;
            card_in_hako[j].insert(i);
            hako_with_card[i].insert(j);
        }else if (n == 2){
            auto itr = card_in_hako[i].begin();
            for (int k = 0; k < card_in_hako[i].size()-1; k++){
                cout << *itr << ' ';
                itr++;
            }
            cout << *itr << endl;
        }else {
            auto it = hako_with_card[i].begin();
            for (int k = 0; k < hako_with_card[i].size()-1; k++){
                cout << *it << ' ';
                it++;
            }
            cout << *it << endl;
        }
    }
    return 0;
}