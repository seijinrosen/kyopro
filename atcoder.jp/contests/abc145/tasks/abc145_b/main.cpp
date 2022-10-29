#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  string S;
  cin >> N >> S;

  int m = N / 2;
  bool ans = S.substr(0, m) == S.substr(m);

  cout << (ans ? "Yes" : "No") << endl;
}
