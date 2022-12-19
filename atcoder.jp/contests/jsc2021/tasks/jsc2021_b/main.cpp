#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(const vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

template <typename T>
set<T> new_set(const vector<T> &vec) {
  return {vec.begin(), vec.end()};
}

template <typename T>
set<T> symmetric_difference(const set<T> &set1, const set<T> &set2) {
  set<T> result;
  set_symmetric_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),
                           inserter(result, result.end()));
  return result;
}

template <typename C, typename T = typename C::value_type>
vector<T> to_vector(const C &container) {
  return {container.begin(), container.end()};
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;
  auto A = input_vector(N);
  auto B = input_vector(M);

  auto ans = to_vector(symmetric_difference(new_set(A), new_set(B)));
  print(ans);
}
