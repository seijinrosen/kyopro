#include <bits/stdc++.h>
using namespace std;

int div_ceil(int a, int b) { return (a + b - 1) / b; }

int main() {
  int N, D;
  cin >> N >> D;

  int ans = div_ceil(N, 2 * D + 1);

  cout << ans << endl;
}
