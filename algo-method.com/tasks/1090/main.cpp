#include <bits/stdc++.h>
using namespace std;

bool even(int n) { return n % 2 == 0; }

int main() {
  int H, W, P, Q;
  cin >> H >> W >> P >> Q;

  string ans = even(P + Q) ? "Black" : "White";

  cout << ans << endl;
}
