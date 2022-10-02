#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename T>
bool contains(const vector<T> &vec, T value) {
  for (auto &&x : vec)
    if (x == value) return true;
  return false;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, X;
  cin >> N >> X;
  auto A = input_vector(N);

  bool ans = contains(A, X);
  print(yes_no(ans));
}
