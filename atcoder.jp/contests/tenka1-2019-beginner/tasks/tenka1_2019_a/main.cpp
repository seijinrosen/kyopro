#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  bool ans = (A < C && C < B) || (B < C && C < A);
  cout << (ans ? "Yes" : "No") << endl;
}
