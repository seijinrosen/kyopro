#include <bits/stdc++.h>
using namespace std;

template <typename T>
vector<T> sort(const vector<T> &vec, bool reverse = false) {
  vector<T> ret = {vec.begin(), vec.end()};
  if (reverse)
    sort(ret.begin(), ret.end(), greater());
  else
    sort(ret.begin(), ret.end());
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  auto ABCD = sort(input_vector(4));
  int A = ABCD[0];
  int B = ABCD[1];
  int C = ABCD[2];
  int D = ABCD[3];

  bool ans = A + B + C == D || A + D == B + C;
  cout << (ans ? "Yes" : "No") << endl;
}
