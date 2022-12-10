#include <bits/stdc++.h>
using namespace std;

bool solve(const string &s) {
  if (s.size() != 8) return false;
  if (!isupper(s.front())) return false;
  if (!isupper(s.back())) return false;
  try {
    int n = stoi(s.substr(1, 6));
    return 100000 <= n && n <= 999999;
  } catch (const std::exception &e) {
    return false;
  }
}

int main() {
  string S;
  cin >> S;

  cout << (solve(S) ? "Yes" : "No") << endl;
}
