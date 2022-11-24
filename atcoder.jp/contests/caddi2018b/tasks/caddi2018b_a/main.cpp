#include <bits/stdc++.h>
using namespace std;

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

int main() {
  string N;
  cin >> N;

  cout << count('2', N) << endl;
}
