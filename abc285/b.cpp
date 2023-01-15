#include<iostream>
#include<string>
using namespace std;

int main(){
    int N;
    string S;
    int l;
    
    cin >> N;
    cin >> S;
    int prev = N-1;
    for (int i = 1; i<N; i++){
        l = 0;
        bool invalid = false;
        while(l<= prev){
            for(int k = 1; k<l+1; k++){
                if (S[k-1] == S[k+i-1]){
                    invalid = true;
                    break;
                }
            }
            if (invalid) break;
            l++;
        }
        prev = l-1;
        cout << l-1 << endl;
    }
    
    return 0;
}