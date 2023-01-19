#include <bits/stdc++.h>
using namespace std;

vector<pair<char, char>> zip(const string &a, const string &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<char, char>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}

int main() {
  string S;
  cin >> S;

  int ans = 0;
  for (auto &&[ch1, ch2] : zip(S, "CODEFESTIVAL2016")) ans += ch1 != ch2;

  cout << ans << endl;
}
