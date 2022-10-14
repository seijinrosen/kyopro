#include <bits/stdc++.h>
using namespace std;

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

int main() {
  int R, D, X2000;
  cin >> R >> D >> X2000;

  int x = X2000;

  for (auto &&_ : range(10)) {
    cout << (x = R * x - D) << endl;
  }
}
