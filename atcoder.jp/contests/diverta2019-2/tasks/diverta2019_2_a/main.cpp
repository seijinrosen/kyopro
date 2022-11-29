#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  int ans = K == 1 ? 0 : N - K;
  cout << ans << endl;
}
