#include <bits/stdc++.h>
using namespace std;

vector<int> scanl_max(const vector<int> &vec) {
  vector<int> result(vec.size());
  partial_sum(vec.begin(), vec.end(), result.begin(),
              [](int a, int b) { return max(a, b); });
  return result;
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

  auto ans = scanl_max(A);
  for (auto &&i : ans) cout << i << endl;
}
