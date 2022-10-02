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

string yes_no(bool b) { return b ? "Yes" : "No"; }

int main() {
  int A, B;
  cin >> A >> B;

  bool ans = false;
  for (auto &&i : range(A, B + 1))
    if (100 % i == 0) ans = true;

  print(yes_no(ans));
}
