#include <bits/stdc++.h>
using namespace std;

template <typename K, typename V>
map<K, V> new_map(const vector<pair<K, V>> &vec) {
  return {vec.begin(), vec.end()};
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

using Pair = pair<string, int>;

vector<Pair> input_pair_vector(int n) {
  vector<Pair> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;
  auto FC = input_pair_vector(N);
  auto X = input_vector<string>(M);

  auto menu = new_map(FC);

  int ans = 0;
  for (auto &&x : X) ans += menu[x];

  cout << ans << endl;
}
