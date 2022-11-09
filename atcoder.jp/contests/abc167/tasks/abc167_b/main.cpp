#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C, K;
  cin >> A >> B >> C >> K;

  int a = min(A, K);
  int b = min(B, K - a);
  int c = K - a - b;
  int ans = a - c;

  cout << ans << endl;
}
