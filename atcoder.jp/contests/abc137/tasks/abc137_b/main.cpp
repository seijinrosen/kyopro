#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(const vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

int main() {
  int K, X;
  cin >> K >> X;

  auto ans = range(X - K + 1, X + K);
  print(ans);
}
