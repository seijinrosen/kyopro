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
vector<T> sort(const vector<T> &vec, bool reverse = false) {
  vector<T> ret = {vec.begin(), vec.end()};
  if (reverse)
    sort(ret.begin(), ret.end(), greater());
  else
    sort(ret.begin(), ret.end());
  return ret;
}

template <typename T>
vector<T> step2(const vector<T> &vec) {
  vector<T> ret;
  for (size_t i = 0; i < vec.size(); i++)
    if (i % 2 == 0) ret.push_back(vec[i]);
  return ret;
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

template <typename T>
vector<T> tail(const vector<T> &vec) {
  return {vec.begin() + 1, vec.end()};
}

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);

  auto sorted_A = sort(A, true);
  int alice = sum(step2(sorted_A));
  int bob = sum(step2(tail(sorted_A)));
  int ans = alice - bob;

  print(ans);
}
