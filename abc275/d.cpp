#include <iostream>
#include <map>
using namespace std;

map<long long, long long> memo;

long long f(long long n){
    if (n == 0) {
        return 1;
    }
    if (memo[n] != 0) return memo[n];
    long long ans = f(n/2) + f(n/3);
    memo[n] = ans;
    return ans;
}
int main(){
    long long N;
    cin >> N;

    cout << f(N) << endl;
    return 0;
}