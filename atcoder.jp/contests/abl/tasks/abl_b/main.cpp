#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ll A, B, C, D;
  cin >> A >> B >> C >> D;

  cout << (max(A, C) <= min(B, D) ? "Yes" : "No") << endl;
}
