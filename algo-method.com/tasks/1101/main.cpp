#include <bits/stdc++.h>
using namespace std;

vector<int> accumulateMax(const vector<int> &vec) {
  size_t n = vec.size();
  vector<int> acc(n);
  acc[0] = vec[0];
  for (size_t i = 1; i < n; i++) acc[i] = max(acc[i - 1], vec[i]);
  return acc;
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

  auto ans = accumulateMax(A);
  for (auto &&i : ans) cout << i << endl;
}
