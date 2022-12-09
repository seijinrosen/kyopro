#include <bits/stdc++.h>
using namespace std;

bool solve(const string &s) {
  if (s == "hi") return true;
  return s.substr(0, 2) == "hi" && solve(s.substr(2));
}

int main() {
  string S;
  cin >> S;

  cout << (solve(S) ? "Yes" : "No") << endl;
}
