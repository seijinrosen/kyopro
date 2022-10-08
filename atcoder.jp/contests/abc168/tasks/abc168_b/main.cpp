#include <bits/stdc++.h>
using namespace std;

string take(int n, const string &s) { return s.substr(0, n); }

int main() {
  int K;
  string S;
  cin >> K >> S;

  string ans = S.size() <= K ? S : take(K, S) + "...";

  cout << ans << endl;
}
