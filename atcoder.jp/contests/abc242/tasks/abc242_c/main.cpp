#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

template <typename T>
void print(T value) {
  cout << value << endl;
}

const int MOD = 998244353;
int plus_mod(int x, int y) { return (x + y) % MOD; }

int main() {
  int N;
  cin >> N;

  vector<vector<int>> dp(N, vector<int>(10));
  dp[0] = {0, 1, 1, 1, 1, 1, 1, 1, 1, 1};

  rep(i, N - 1) {
    for (int x = 1; x <= 9; x++) {
      dp[i + 1][x] = plus_mod(dp[i + 1][x], dp[i][x]);
      if (x != 1) dp[i + 1][x - 1] = plus_mod(dp[i + 1][x - 1], dp[i][x]);
      if (x != 9) dp[i + 1][x + 1] = plus_mod(dp[i + 1][x + 1], dp[i][x]);
    }
  }

  int ans = 0;
  for (auto &&i : dp[N - 1]) ans = plus_mod(ans, i);

  print(ans);
}
