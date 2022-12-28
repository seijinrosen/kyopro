#include <bits/stdc++.h>
using namespace std;

bool is_palindrome(const string &s) {
  string reversed = {s.rbegin(), s.rend()};
  return s == reversed;
}

string rstrip(const string &s, char c) {
  int n = s.size();
  for (int i = n - 1; i >= 0; i--) {
    if (s[i] != c) break;
    n--;
  }
  return s.substr(0, n);
}

int main() {
  string N;
  cin >> N;

  bool ans = is_palindrome(rstrip(N, '0'));
  cout << (ans ? "Yes" : "No") << endl;
}
