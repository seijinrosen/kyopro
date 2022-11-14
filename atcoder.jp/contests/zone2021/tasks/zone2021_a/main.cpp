#include <bits/stdc++.h>
using namespace std;

int count(const string &count_string, const string &s) {
  int ret = 0;
  for (size_t i = 0; i < s.size(); i++)
    if (s.substr(i, count_string.size()) == count_string) ret++;
  return ret;
}

int main() {
  string S;
  cin >> S;

  int ans = count("ZONe", S);
  cout << ans << endl;
}
