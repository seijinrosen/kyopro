#include <bits/stdc++.h>
using namespace std;

template <typename T>
set<T> new_set(const vector<T> &vec) {
  return {vec.begin(), vec.end()};
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);

  bool ans = new_set(A).size() == N;
  cout << (ans ? "YES" : "NO") << endl;
}
