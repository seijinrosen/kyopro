#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

int main() {
  int N, X;
  cin >> N >> X;

  int ans = 0;
  for (auto &&i : range(N))
    if (0 < ((1 << i) & X)) ans++;

  print(ans);
}
