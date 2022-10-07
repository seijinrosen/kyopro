#define _GLIBCXX_DEBUG
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

  string ans = repeat("x", S.size());

  print(ans);
}
