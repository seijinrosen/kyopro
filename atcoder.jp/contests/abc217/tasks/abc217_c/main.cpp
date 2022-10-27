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

template <typename T>
vector<pair<int, T>> enumerate(const vector<T> &vec, int start = 0) {
  vector<pair<int, T>> ret(vec.size());
  for (size_t i = 0; i < vec.size(); i++) ret[i] = {start + i, vec[i]};
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto P = input_vector(N);

  vector<int> ans(N);
  for (auto &&[i, p] : enumerate(P, 1)) ans[p - 1] = i;

  print(ans);
}
