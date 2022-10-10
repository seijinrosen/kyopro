#include <bits/stdc++.h>
using namespace std;

bool is_leap_year(int n) {
  if (n % 400 == 0) return true;
  if (n % 100 == 0) return false;
  if (n % 4 == 0) return true;
  return false;
}

int main() {
  int N;
  cin >> N;

  bool ans = is_leap_year(N);

  cout << (ans ? "Yes" : "No") << endl;
}
