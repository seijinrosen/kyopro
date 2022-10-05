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
set<T> difference(const set<T> &set_a, const set<T> &set_b) {
  set<T> result;
  set_difference(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(),
                 inserter(result, result.end()));
  return result;
}

template <typename T>
T head(const set<T> &st) {
  return *st.begin();
}

template <typename T>
set<T> new_set(const vector<T> &vec) {
  return {vec.begin(), vec.end()};
}

// input functions -------------------------------------------------------------
template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  auto S = input_vector<string>(3);

  set<string> contests = {"ABC", "ARC", "AGC", "AHC"};
  auto ans = difference(contests, new_set(S));

  print(head(ans));
}
