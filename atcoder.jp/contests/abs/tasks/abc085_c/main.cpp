#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T1, typename T2, typename T3>
void print(const tuple<T1, T2, T3> &t) {
  cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
}
// print functions -------------------------------------------------------------

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

tuple<int, int, int> solve(int n, int y) {
  for (auto &&i : range(n + 1))
    for (auto &&j : range(n - i + 1)) {
      int k = n - i - j;
      if (10000 * i + 5000 * j + 1000 * k == y) return {i, j, k};
    }
  return {-1, -1, -1};
};

int main() {
  int N, Y;
  cin >> N >> Y;

  auto ans = solve(N, Y);
  print(ans);
}
