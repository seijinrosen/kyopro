#include <bits/stdc++.h>
using namespace std;

template <typename T>
vector<T> sort(const vector<T> &vec, bool reverse = false) {
  vector<T> ret = {vec.begin(), vec.end()};
  if (reverse)
    sort(ret.begin(), ret.end(), greater());
  else
    sort(ret.begin(), ret.end());
  return ret;
}

vector<pair<int, int>> input_pair_vector(int n) {
  vector<pair<int, int>> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;
  auto AB = input_pair_vector(M);

  vector<vector<int>> G(N);
  for (auto &&[a, b] : AB) {
    G[a - 1].push_back(b);
    G[b - 1].push_back(a);
  }

  for (auto &&g : G) {
    cout << g.size();
    for (auto &&x : sort(g)) cout << ' ' << x;
    cout << endl;
  }
}
