#include <bits/stdc++.h>
using namespace std;

int div_ceil(int a, int b) { return (a + b - 1) / b; }

int main() {
  int X, Y, Z;
  cin >> X >> Y >> Z;

  int ans = div_ceil(Y * Z, X) - 1;
  cout << ans << endl;
}
