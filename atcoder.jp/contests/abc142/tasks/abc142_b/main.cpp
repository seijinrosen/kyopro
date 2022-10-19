#include <bits/stdc++.h>
using namespace std;

template <typename P, typename T>
int count(P pred, const vector<T> &vec) {
  return count_if(vec.begin(), vec.end(), pred);
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, K;
  cin >> N >> K;
  auto H = input_vector(N);

  int ans = count([&](int h) { return K <= h; }, H);
  cout << ans << endl;
}
