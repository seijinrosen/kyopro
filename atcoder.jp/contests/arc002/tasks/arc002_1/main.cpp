#include <bits/stdc++.h>
using namespace std;

bool is_leap(int y) {
  if (y % 400 == 0) return true;
  if (y % 100 == 0) return false;
  return y % 4 == 0;
}

int main() {
  int Y;
  cin >> Y;

  cout << (is_leap(Y) ? "YES" : "NO") << endl;
}
