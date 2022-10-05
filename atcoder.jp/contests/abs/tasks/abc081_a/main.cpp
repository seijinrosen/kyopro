#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

int main() {
  string S;
  cin >> S;

  int ans = count('1', S);
  print(ans);
}
