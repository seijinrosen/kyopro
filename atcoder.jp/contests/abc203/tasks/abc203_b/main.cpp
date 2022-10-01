#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

int main() {
  int N, K;
  cin >> N >> K;

  int ans = 0;
  for (auto &&i : range(1, N + 1))
    for (auto &&j : range(1, K + 1)) ans += 100 * i + j;

  print(ans);
}
