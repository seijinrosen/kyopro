#include <bits/stdc++.h>
using namespace std;

int ctoi(char c) { return c - '0'; }

int main() {
  string N;
  cin >> N;

  int total = 0;
  for (auto &&c : N) total += ctoi(c);

  bool ans = total % 9 == 0;
  cout << (ans ? "Yes" : "No") << endl;
}
