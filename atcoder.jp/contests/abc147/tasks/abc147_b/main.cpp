#include <bits/stdc++.h>
using namespace std;

template <typename P, typename T>
vector<T> filter(P pred, const vector<T> &vec) {
  vector<T> ret;
  for (auto &&x : vec)
    if (pred(x)) ret.push_back(x);
  return ret;
}

string reverse(const string &s) { return {s.rbegin(), s.rend()}; }

vector<pair<char, char>> zip(const string &a, const string &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<char, char>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}

int main() {
  string S;
  cin >> S;

  int ans = filter([](pair<char, char> p) { return p.first != p.second; },
                   zip(S, reverse(S)))
                .size() /
            2;

  cout << ans << endl;
}
