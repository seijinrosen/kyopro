#include <bits/stdc++.h>
using namespace std;

bool contains(const string &search_string, const string &s) {
  for (size_t i = 0; i < s.size(); i++)
    if (s.substr(i, search_string.size()) == search_string) return true;
  return false;
}

int main() {
  string S;
  cin >> S;

  cout << (contains("AC", S) ? "Yes" : "No") << endl;
}
