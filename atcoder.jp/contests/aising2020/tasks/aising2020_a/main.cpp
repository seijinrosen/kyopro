#include <bits/stdc++.h>
using namespace std;

int main() {
  int L, R, D;
  cin >> L >> R >> D;

  int ans = R / D - (L - 1) / D;
  cout << ans << endl;
}
