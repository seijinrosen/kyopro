#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, K;
  cin >> N >> K;
  auto P = input_vector(N);
  auto Q = input_vector(N);

  bool ans = false;
  for (auto &&p : P)
    for (auto &&q : Q)
      if (p + q == K) ans = true;

  print(yes_no(ans));
}
