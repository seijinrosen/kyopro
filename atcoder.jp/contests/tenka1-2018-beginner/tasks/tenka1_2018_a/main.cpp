#include <bits/stdc++.h>
using namespace std;

string reverse(const string &s) { return {s.rbegin(), s.rend()}; }

int main() {
  string S;
  cin >> S;

  string ans = S.size() == 2 ? S : reverse(S);
  cout << ans << endl;
}
