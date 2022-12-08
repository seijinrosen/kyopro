#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  string S;
  cin >> N >> S >> K;

  string ans = "";
  for (auto &&c : S) ans += c == S[K - 1] ? c : '*';

  cout << ans << endl;
}
