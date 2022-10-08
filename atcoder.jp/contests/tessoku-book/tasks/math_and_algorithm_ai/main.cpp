#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

vector<int> accumulate(const vector<int> &vec) {
  size_t n = vec.size();
  vector<int> acc(n + 1);
  for (size_t i = 0; i < n; i++) acc[i + 1] = acc[i] + vec[i];
  return acc;
}

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
vector<pair<int, int>> input_pair_vector(int n) {
  vector<pair<int, int>> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N, Q;
  cin >> N >> Q;
  auto A = input_vector(N);
  auto LR = input_pair_vector(Q);

  auto acc = accumulate(A);
  for (auto &&[l, r] : LR) print(acc[r] - acc[l - 1]);
}
