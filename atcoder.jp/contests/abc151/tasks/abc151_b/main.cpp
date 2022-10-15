#include <bits/stdc++.h>
using namespace std;

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, K, M;
  cin >> N >> K >> M;
  auto A = input_vector(N - 1);

  int x = N * M - sum(A);
  int ans = K < x ? -1 : max(x, 0);

  cout << ans << endl;
}
