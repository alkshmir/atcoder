#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> P(N);
  for (int i = 0; i < N; i++) {
    cin >> P.at(i);
  }
  prev_permutation(P.begin(), P.end());
  //cout << N << endl;
  copy(P.begin(),P.end(),
        ostream_iterator<int>(cout," "));

  cout << endl;


  return 0; 
}