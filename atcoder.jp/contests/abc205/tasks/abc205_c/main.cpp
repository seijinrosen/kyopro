#include <bits/stdc++.h>
using namespace std;

char solve(int a, int b, int c) {
  if (c % 2 == 0) {
    if (abs(a) < abs(b)) return '<';
    if (abs(a) > abs(b)) return '>';
    return '=';
  }
  if (a < b) return '<';
  if (a > b) return '>';
  return '=';
}

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  cout << solve(A, B, C) << endl;
}
