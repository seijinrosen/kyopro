#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ll A, B, C, D;
  cin >> A >> B >> C >> D;

  ll ans = max({A * C, A * D, B * C, B * D});
  cout << ans << endl;
}
