#include <bits/stdc++.h>
using namespace std;

vector<pair<char, char>> zip(const string &a, const string &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<char, char>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}

int main() {
  int N;
  string S, T;
  cin >> N >> S >> T;

  string ans = "";
  for (auto &&[s, t] : zip(S, T)) ans = ans + s + t;

  cout << ans << endl;
}
