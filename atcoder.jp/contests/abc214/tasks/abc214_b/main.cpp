#include <bits/stdc++.h>
using namespace std;

int main() {
  int S, T;
  cin >> S >> T;

  int ans = 0;
  for (size_t a = 0; a <= S; a++)
    for (size_t b = 0; b <= S - a; b++)
      for (size_t c = 0; c <= S - a - b; c++)
        if (a * b * c <= T) ans++;

  cout << ans << endl;
}
