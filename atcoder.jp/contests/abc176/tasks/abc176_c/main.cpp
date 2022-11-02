#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename T>
vector<T> scanl1(function<T(T, T)> func, const vector<T> &vec) {
  vector<T> result(vec.size());
  partial_sum(vec.begin(), vec.end(), result.begin(), func);
  return result;
}

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
  auto A = input_vector(N);

  auto acc_max = scanl1<int>([](int a, int b) { return max(a, b); }, A);

  ll ans = 0;
  for (auto &&[a, b] : zip(acc_max, A)) ans += a - b;

  cout << ans << endl;
}
