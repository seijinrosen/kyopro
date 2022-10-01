#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename T>
vector<pair<int, T>> enumerate(const vector<T> &vec) {
  vector<pair<int, T>> ret(vec.size());
  for (size_t i = 0; i < vec.size(); i++) ret[i] = {i, vec[i]};
  return ret;
}

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;
  auto W = input_vector(N);

  vector dp(N + 1, vector<pair<bool, bool>>(M + 1, {false, false}));
  dp[0][0].first = true;

  for (auto &&[i, w] : enumerate(W)) {
    for (auto &&j : range(M + 1)) {
      dp[i + 1][j].first |= dp[i][j].first;
      dp[i + 1][j].second |= dp[i][j].second;

      if (j + w <= M) {
        dp[i + 1][j + w].second |= dp[i][j].first;
        dp[i + 1][j + w].first |= dp[i][j].second;
      }
    }
  }

  bool ans = dp[N][M].second;
  print(yes_no(ans));
}
