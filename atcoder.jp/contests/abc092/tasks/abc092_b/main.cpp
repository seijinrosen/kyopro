#include <bits/stdc++.h>
using namespace std;

int div_ceil(int a, int b) { return (a + b - 1) / b; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, D, X;
  cin >> N >> D >> X;
  auto A = input_vector(N);

  int ans = X;
  for (auto &&a : A) ans += div_ceil(D, a);

  cout << ans << endl;
}
