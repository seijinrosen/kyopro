#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

template <typename T>
vector<T> sorted(const vector<T> &vec) {
  vector<T> ret = {vec.begin(), vec.end()};
  sort(ret.begin(), ret.end());
  return ret;
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

template <typename T>
vector<T> take(int n, const vector<T> &vec) {
  return {vec.begin(), vec.begin() + n};
}

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N, K;
  cin >> N >> K;
  auto P = input_vector(N);

  int ans = sum(take(K, sorted(P)));
  print(ans);
}
