#include <bits/stdc++.h>
using namespace std;

int main() {
  char S, T;
  cin >> S >> T;

  char ans = S == 'Y' ? toupper(T) : T;
  cout << ans << endl;
}
