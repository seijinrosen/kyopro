#include <bits/stdc++.h>
using namespace std;

int main() {
  int X, Y, Z;
  cin >> X >> Y >> Z;

  int ans = (X - Z) / (Y + Z);

  cout << ans << endl;
}
