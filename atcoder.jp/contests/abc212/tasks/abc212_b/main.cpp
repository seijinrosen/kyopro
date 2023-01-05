#include <bits/stdc++.h>
using namespace std;

template <typename T>
set<T> new_set(const vector<T> &vec) {
  return {vec.begin(), vec.end()};
}

template <typename T>
vector<pair<T, T>> pairwise(const vector<T> &vec) {
  size_t n = vec.size() - 1;
  vector<pair<T, T>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {vec[i], vec[i + 1]};
  return ret;
}

vector<int> string_to_digits(const string &s) {
  vector<int> digits;
  for (auto &&c : s) digits.push_back(c - '0');
  return digits;
}

bool is_weak1(const vector<int> &digits) { return new_set(digits).size() == 1; }

bool is_weak2(const vector<int> &digits) {
  for (auto &&[x, y] : pairwise(digits))
    if ((x + 1) % 10 != y) return false;
  return true;
}

int main() {
  string XS;
  cin >> XS;

  auto digits = string_to_digits(XS);

  cout << (is_weak1(digits) || is_weak2(digits) ? "Weak" : "Strong") << endl;
}
