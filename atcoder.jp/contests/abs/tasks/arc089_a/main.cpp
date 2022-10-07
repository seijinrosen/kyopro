#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

template <typename P, typename T>
bool all(P pred, const vector<T> &vec) {
  for (auto &&x : vec)
    if (!pred(x)) return false;
  return true;
}

bool even(int n) { return n % 2 == 0; }

template <typename T>
vector<pair<T, T>> pairwise(const vector<T> &vec) {
  size_t n = vec.size() - 1;
  vector<pair<T, T>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {vec[i], vec[i + 1]};
  return ret;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

// input functions -------------------------------------------------------------
vector<tuple<int, int, int>> input_vector(int n) {
  vector<tuple<int, int, int>> ret(n);
  for (auto &&[a, b, c] : ret) cin >> a >> b >> c;
  return ret;
}
// input functions -------------------------------------------------------------

using info = tuple<int, int, int>;

bool ok(const pair<info, info> &p) {
  auto [t1, x1, y1] = p.first;
  auto [t2, x2, y2] = p.second;
  int time = t2 - t1 - abs(x2 - x1) - abs(y2 - y1);
  return 0 <= time && even(time);
}

int main() {
  int N;
  cin >> N;
  auto TXY = input_vector(N);

  TXY.insert(TXY.begin(), {0, 0, 0});
  bool ans = all(ok, pairwise(TXY));

  print(yes_no(ans));
}
