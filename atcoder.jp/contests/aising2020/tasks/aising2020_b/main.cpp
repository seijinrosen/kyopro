#include <bits/stdc++.h>
using namespace std;

bool odd(int n) { return n % 2 == 1; }

int main() {
  int N;
  cin >> N;

  vector<int> A(N);
  for (auto &&a : A) cin >> a;

  int ans = 0;
  for (int i = 0; i < N; i += 2) ans += odd(A[i]);

  cout << ans << endl;
}
