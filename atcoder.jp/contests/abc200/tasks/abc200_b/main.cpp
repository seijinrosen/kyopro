#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll func(ll n) {
  if (n % 200 == 0) return n / 200;
  return 1000 * n + 200;
}

int main() {
  int N, K;
  cin >> N >> K;

  ll n = N;
  for (size_t i = 0; i < K; i++) n = func(n);

  cout << n << endl;
}
