#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int b = min(5, N);
  int a = N - b;
  int ans = A * a + B * b;

  cout << ans << endl;
}
