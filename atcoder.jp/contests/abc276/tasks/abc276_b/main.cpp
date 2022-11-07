#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> input_pair_vector(int n) {
  vector<pair<int, int>> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;
  auto AB = input_pair_vector(M);

  vector<set<int>> G(N);
  for (auto &&[a, b] : AB) {
    G[a - 1].insert(b);
    G[b - 1].insert(a);
  }

  for (auto &&g : G) {
    cout << g.size();
    for (auto &&x : g) cout << ' ' << x;
    cout << endl;
  }
}
