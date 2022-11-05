#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  size_t i = S.find_last_of('a');
  int ans = i == -1 ? -1 : i + 1;

  cout << ans << endl;
}
