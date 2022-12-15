#include <bits/stdc++.h>
using namespace std;

bool is_product_day(int m, int d) {
  int d10 = d / 10;
  int d1 = d % 10;
  return (d1 >= 2) && (d10 >= 2) && (d1 * d10 == m);
}

int solve(int m, int d) {
  int ans = 0;
  for (int mm = 1; mm <= m; mm++)
    for (int dd = 1; dd <= d; dd++)
      if (is_product_day(mm, dd)) ans++;
  return ans;
}

int main() {
  int M, D;
  cin >> M >> D;

  cout << solve(M, D) << endl;
}
