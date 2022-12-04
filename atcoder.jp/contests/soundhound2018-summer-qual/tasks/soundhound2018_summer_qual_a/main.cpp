#include <bits/stdc++.h>
using namespace std;

char solve(int a, int b) {
  if (a + b == 15) return '+';
  if (a * b == 15) return '*';
  return 'x';
}

int main() {
  int a, b;
  cin >> a >> b;

  cout << solve(a, b) << endl;
}
