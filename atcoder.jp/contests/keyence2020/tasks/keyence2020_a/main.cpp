#include <bits/stdc++.h>
using namespace std;

int div_ceil(int a, int b) { return (a + b - 1) / b; }

int main() {
  int H, W, N;
  cin >> H >> W >> N;

  int ans = div_ceil(N, max(H, W));
  cout << ans << endl;
}
