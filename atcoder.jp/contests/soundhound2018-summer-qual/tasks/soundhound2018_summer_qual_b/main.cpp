#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  int w;
  cin >> S >> w;

  string ans = "";
  for (int i = 0; i < S.size(); i += w) {
    ans += S[i];
  }

  cout << ans << endl;
}
