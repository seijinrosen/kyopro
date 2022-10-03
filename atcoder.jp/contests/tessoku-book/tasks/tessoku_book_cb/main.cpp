#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

template <typename T>
vector<tuple<T, T, T>> combinations3(const vector<T> &vec) {
  size_t n = vec.size();
  vector<tuple<T, T, T>> ret;
  for (size_t i = 0; i < n - 2; i++)
    for (size_t j = i + 1; j < n - 1; j++)
      for (size_t k = j + 1; k < n; k++)
        ret.push_back({vec[i], vec[j], vec[k]});
  return ret;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);

  bool ans = false;
  for (auto &&[a, b, c] : combinations3(A))
    if (a + b + c == 1000) ans = true;

  print(yes_no(ans));
}
