#include <bits/stdc++.h>
using namespace std;

template <typename T>
vector<T> reverse(const vector<T> &vec) {
  return {vec.rbegin(), vec.rend()};
}

template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto S = input_vector<string>(N);

  for (auto &&s : reverse(S)) {
    cout << s << endl;
  }
}
