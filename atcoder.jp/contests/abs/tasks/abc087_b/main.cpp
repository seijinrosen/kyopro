#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;

  int ans = 0;
  for (auto &&a : range(A + 1))
    for (auto &&b : range(B + 1))
      for (auto &&c : range(C + 1))
        if (500 * a + 100 * b + 50 * c == X) ans++;

  print(ans);
}
