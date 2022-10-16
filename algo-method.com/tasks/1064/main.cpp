#include <bits/stdc++.h>
using namespace std;

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int H, W;
  cin >> H >> W;
  auto S = input_vector<string>(H);

  int ans = 0;
  for (auto &&s : S) ans += count('o', s);

  cout << ans << endl;
}
