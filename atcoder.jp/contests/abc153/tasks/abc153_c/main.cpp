#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  int N, K;
  cin >> N >> K;
  vector<int> H(N);
  for (auto &&i : H) cin >> i;

  sort(H.begin(), H.end());
  reverse(H.begin(), H.end());

  ll ans = 0;
  for (int i = K; i < N; i++) ans += H[i];

  cout << ans << endl;
}
