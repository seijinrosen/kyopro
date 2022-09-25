#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string repeat(const string &s, int n) {
  string ret;
  for (size_t i = 0; i < n; i++) ret += s;
  return ret;
}

int main() {
  string S;
  cin >> S;

  string X = repeat("WBWBWWBWBWBW", 2);
  vector<string> Y = {
      "Do",  "Do#", "Re",  "Re#", "Mi",  "Fa",
      "Fa#", "So",  "So#", "La",  "La#", "Si",
  };

  map<string, string> mp;
  for (size_t i = 0; i < 12; i++) mp[X.substr(i, 12)] = Y[i];

  string ans = mp[S.substr(0, 12)];
  print(ans);
}
