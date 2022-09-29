#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  auto S = input_vector<string>(4);

  bool ans = set(S.begin(), S.end()).size() == 4;
  print(yes_no(ans));
}
