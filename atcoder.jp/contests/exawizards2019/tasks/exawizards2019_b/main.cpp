#include <bits/stdc++.h>
using namespace std;

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

int main() {
  int N;
  string S;
  cin >> N >> S;

  bool ans = count('B', S) < count('R', S);
  cout << (ans ? "Yes" : "No") << endl;
}
