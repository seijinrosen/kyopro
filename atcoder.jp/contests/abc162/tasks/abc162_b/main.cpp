#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename P, typename T>
vector<T> filter(P pred, const vector<T> &vec) {
  vector<T> ret;
  for (auto &&x : vec)
    if (pred(x)) ret.push_back(x);
  return ret;
}

vector<ll> range(int start, int stop) {
  vector<ll> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

int main() {
  int N;
  cin >> N;

  ll ans = sum(
      filter([](ll i) { return i % 3 != 0 && i % 5 != 0; }, range(1, N + 1)));

  cout << ans << endl;
}
