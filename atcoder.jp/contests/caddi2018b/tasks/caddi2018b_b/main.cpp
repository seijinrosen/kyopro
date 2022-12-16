#include <bits/stdc++.h>
using namespace std;

using Pair = pair<int, int>;
vector<Pair> input_pair_vector(int n) {
  vector<Pair> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}

int main() {
  int N, H, W;
  cin >> N >> H >> W;
  auto AB = input_pair_vector(N);

  int ans = 0;
  for (auto &&[a, b] : AB)
    if (H <= a && W <= b) ans++;

  cout << ans << endl;
}
