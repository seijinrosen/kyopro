#include <bits/stdc++.h>
using namespace std;

int relu(int x) {
  if (x >= 0) return x;
  return 0;
}

int main() {
  int x;
  cin >> x;

  int ans = relu(x);

  cout << ans << endl;
}
