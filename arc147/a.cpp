#include <iostream>
#include <set>
using namespace std;

int main(){
    int N;
    cin >> N;
    multiset<int> A;
    int j;
    for (int i = 0; i < N; i++){
        cin >> j;
        A.insert(j);
    }
    int64_t cnt = 0;
    while (A.size() != 1){
        auto st = A.begin();
        auto end = A.end();
        int e = *(--end);
        //cout << "begin:" << *st << " end:" << e << endl;
        //cout << "A.size() = " << A.size() << endl;
        
        if ( e % *st!= 0) A.insert(e % *st);
        //cout << e << endl;
        auto itr = A.find(e);
        if (itr != A.end()) A.erase(itr);
        cnt++;
    }
    cout << cnt << endl;

    return 0;
}