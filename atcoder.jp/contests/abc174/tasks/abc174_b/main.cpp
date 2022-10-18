#include <bits/stdc++.h>
using namespace std;

template <typename P, typename T>
int count(P pred, const vector<T> &vec) {
  return count_if(vec.begin(), vec.end(), pred);
}

template <typename T1, typename T2>
vector<pair<T1, T2>> input_pair_vector(int n) {
  vector<pair<T1, T2>> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}

int main() {
  int N, D;
  cin >> N >> D;
  auto XY = input_pair_vector<int, int>(N);

  auto func = [&](const pair<int, int> &p) {
    auto [x, y] = p;
    return pow(x, 2) + pow(y, 2) <= pow(D, 2);
  };

  int ans = count(func, XY);
  cout << ans << endl;
}
