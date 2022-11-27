#include <bits/stdc++.h>
using namespace std;

int additional_prize(int x, int y) {
  if (x == 1 && y == 1) return 400000;
  return 0;
}

int main() {
  int X, Y;
  cin >> X >> Y;

  map<int, int> prize = {{3, 100000}, {2, 200000}, {1, 300000}};
  int ans = prize[X] + prize[Y] + additional_prize(X, Y);

  cout << ans << endl;
}
