#include <bits/stdc++.h>
using namespace std;

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

int main() {
  string S;
  cin >> S;

  cout << (count('x', S) <= 7 ? "YES" : "NO") << endl;
}
