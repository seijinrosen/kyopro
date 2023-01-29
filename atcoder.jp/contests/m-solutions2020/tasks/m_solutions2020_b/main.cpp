#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, K;
  cin >> a >> b >> c >> K;

  for (size_t i = 0; i <= K; i++) {
    if (a < b && b < c) {
      cout << "Yes" << endl;
      return 0;
    }

    if (a >= b) {
      b *= 2;
    } else if (b >= c) {
      c *= 2;
    }
  }

  cout << "No" << endl;
}
