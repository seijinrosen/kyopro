#include <bits/stdc++.h>
using namespace std;

template <typename T>
vector<T> sort(const initializer_list<T> &vec, bool reverse = false) {
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
  int N;
  cin >> N;
  auto P = input_vector(N);

  int ans = 0;
  for (size_t i = 1; i < N - 1; i++)
    if (sort({P[i - 1], P[i], P[i + 1]})[1] == P[i]) ans++;

  cout << ans << endl;
}
