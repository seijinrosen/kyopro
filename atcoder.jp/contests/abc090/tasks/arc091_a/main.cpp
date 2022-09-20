#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  ll N, M;
  cin >> N >> M;

  if (M < N) swap(N, M);

  ll ans = (N - 2) * (M - 2);
  if (N == 1) ans = M == 1 ? 1 : M - 2;

  print(ans);
}
