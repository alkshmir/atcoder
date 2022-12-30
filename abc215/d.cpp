#include <set>
#include <vector>
#include <iostream>
using namespace std;


void prime_factorize(long long n, set<long long>& primes){
    primes.insert(1);
    while(n % 2 == 0){
        primes.insert(2);
        n /= 2;
    }
    long long f = 3;
    while (f*f <= n){
        if (n % f == 0){
            primes.insert(f);
            n /= f;
        }else{
            f += 2;
        }
    }
    if (n != 1) primes.insert(n);
}
/*
long long GCD(unsigned long long a, unsigned long long b) {
    if (b == 0) return a;
    else return GCD(b, a % b);
}
*/
int main(){
    long long N, M;
    cin >> N >> M;
    std::vector<long long> A(N);
    set<long long> primes;
    for (long long i=0; i<N; i++) cin >> A.at(i);
    for (long long i=0; i<N; i++){
        prime_factorize(A[i], primes);
    }
    //cout << "primes: " << primes.size() << endl;
    // 以下の方法では、lが超巨大になるので、64bitでも計算できない。
    /*unsigned long long l=1;
    for (auto x : primes){
        l *= x;
    }
    cout << "l: " << l << endl;
    */
    vector<long long> ans;
    for (long long k = 1; k <= M; k++){
        bool valid = true;
        for (auto p: primes){
            if (p != 1 && k%p == 0){
                valid = false;
                break;
            }
        }
        if (valid) ans.push_back(k);
    }
    cout << ans.size() << endl;
    for (long long i = 0; i < ans.size(); i++){
        cout << ans[i] << endl;
    }

    return 0;
}