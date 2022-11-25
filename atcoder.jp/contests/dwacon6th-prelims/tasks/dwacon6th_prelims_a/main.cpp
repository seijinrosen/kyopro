#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<pair<string, int>> ST(N);
  for (auto &&[s, t] : ST) cin >> s >> t;

  string X;
  cin >> X;

  int ans = 0;
  bool asleep = false;

  for (auto &&[s, t] : ST) {
    if (asleep) ans += t;
    if (s == X) asleep = true;
  }

  cout << ans << endl;
}
