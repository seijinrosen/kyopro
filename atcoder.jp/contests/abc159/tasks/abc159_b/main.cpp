#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

string reverse(string &s) { return string(s.rbegin(), s.rend()); }

string my_slice(string &s, int start, int stop) {
  return s.substr(start, stop - start);
}

bool is_palindrome(string &s) { return s == reverse(s); }

string former(string &s) {
  int n = s.size();
  return my_slice(s, 0, (n - 1) / 2);
}

string latter(string &s) {
  int n = s.size();
  return my_slice(s, (n + 3) / 2 - 1, n);
}

int main() {
  string S;
  cin >> S;

  vector<string> vec = {S, former(S), latter(S)};
  bool ans = all_of(vec.begin(), vec.end(), is_palindrome);

  print(yes_no(ans));
}
