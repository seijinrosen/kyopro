#include <bits/stdc++.h>
using namespace std;

bool contains(const string &search_string, const string &s) {
  for (size_t i = 0; i < s.size(); i++)
    if (s.substr(i, search_string.size()) == search_string) return true;
  return false;
}

int main() {
  string c;
  cin >> c;

  bool ans = contains(c, "OPKL");

  cout << (ans ? "Right" : "Left") << endl;
}
