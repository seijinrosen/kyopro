#include <bits/stdc++.h>
using namespace std;

string repeat(int n, const string &s) {
  string ret;
  for (size_t i = 0; i < n; i++) ret += s;
  return ret;
}

int main() {
  int K;
  cin >> K;

  string ans = repeat(K, "ACL");
  cout << ans << endl;
}
