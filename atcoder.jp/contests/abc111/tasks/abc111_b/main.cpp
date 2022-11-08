#include <bits/stdc++.h>
using namespace std;

int div_ceil(int a, int b) { return (a + b - 1) / b; }

int main() {
  int N;
  cin >> N;

  int ans = div_ceil(N, 111) * 111;
  cout << ans << endl;
}
