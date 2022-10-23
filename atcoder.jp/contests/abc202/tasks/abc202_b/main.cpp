#include <bits/stdc++.h>
using namespace std;

string reverse(const string &s) { return {s.rbegin(), s.rend()}; }

string translate(const map<char, char> &mp, const string &s) {
  string ret;
  for (auto &&c : s) ret += mp.count(c) ? mp.at(c) : c;
  return ret;
}

int main() {
  string S;
  cin >> S;

  map<char, char> d = {{'6', '9'}, {'9', '6'}};
  string ans = translate(d, reverse(S));

  cout << ans << endl;
}
