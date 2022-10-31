#include <bits/stdc++.h>
using namespace std;

template <typename T1, typename T2>
vector<pair<T1, T2>> zip(const vector<T1> &a, const vector<T2> &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<T1, T2>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto V = input_vector(N);
  auto C = input_vector(N);

  int ans = 0;
  for (auto &&[v, c] : zip(V, C)) ans += max(0, v - c);

  cout << ans << endl;
}
