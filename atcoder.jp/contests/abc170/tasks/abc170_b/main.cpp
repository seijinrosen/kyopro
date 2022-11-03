#include <bits/stdc++.h>
using namespace std;

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}

template <typename Predicate, typename T>
bool some(Predicate pred, const vector<T> &vec) {
  return any_of(vec.begin(), vec.end(), pred);
}

int main() {
  int X, Y;
  cin >> X >> Y;

  bool ans =
      some([&](int crane) { return 2 * crane == 4 * X - Y; }, range(X + 1));

  cout << (ans ? "Yes" : "No") << endl;
}
