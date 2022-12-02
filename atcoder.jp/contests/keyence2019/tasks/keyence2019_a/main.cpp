#include <bits/stdc++.h>
using namespace std;

string sort(const string &s, bool reverse = false) {
  string ret = {s.begin(), s.end()};
  if (reverse)
    sort(ret.begin(), ret.end(), greater());
  else
    sort(ret.begin(), ret.end());
  return ret;
}

int main() {
  string N(4, '0');
  for (auto &&c : N) cin >> c;

  bool ans = sort(N) == sort("1974");
  cout << (ans ? "YES" : "NO") << endl;
}
