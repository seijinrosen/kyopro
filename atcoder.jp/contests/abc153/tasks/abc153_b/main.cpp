#include <bits/stdc++.h>
using namespace std;

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int H, N;
  cin >> H >> N;
  auto A = input_vector(N);

  int ans = H <= sum(A);
  cout << yes_no(ans) << endl;
}
