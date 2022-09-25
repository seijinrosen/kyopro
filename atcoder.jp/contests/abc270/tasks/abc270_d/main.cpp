#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, K;
  cin >> N >> K;
  vector<int> A = input_vector(K);

  vector<int> dp(N + 1);

  for (auto &&n : range(1, N + 1)) {
    for (auto &&a : A) {
      if (n < a) break;
      dp[n] = max(dp[n], n - dp[n - a]);
    }
  }

  int ans = dp[N];
  print(ans);
}
