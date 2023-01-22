#include <bits/stdc++.h>
using namespace std;

template <typename T>
T max(const vector<T> &vec) {
  return *max_element(vec.begin(), vec.end());
}

template <typename T>
T min(const vector<T> &vec) {
  return *min_element(vec.begin(), vec.end());
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

  int ans = max(A) - min(A);

  cout << ans << endl;
}
