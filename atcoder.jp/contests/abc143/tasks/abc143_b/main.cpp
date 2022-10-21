#include <bits/stdc++.h>
using namespace std;

template <typename T>
vector<pair<T, T>> combinations2(const vector<T> &vec) {
  size_t x = vec.size() - 2;
  vector<pair<T, T>> ret;
  for (size_t i = 0; i < x + 1; i++)
    for (size_t j = i + 1; j < x + 2; j++) ret.push_back({vec[i], vec[j]});
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
  auto D = input_vector(N);

  int ans = 0;
  for (auto &&[x, y] : combinations2(D)) ans += x * y;

  cout << ans << endl;
}
