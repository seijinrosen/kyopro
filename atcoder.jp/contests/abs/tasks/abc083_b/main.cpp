#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

int sum_of_each_digit(int i) {
  int ret = 0;
  for (auto &&c : to_string(i)) ret += c - '0';
  return ret;
}

int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int ans = 0;
  for (auto &&i : range(1, N + 1)) {
    int s = sum_of_each_digit(i);
    if (A <= s && s <= B) ans += i;
  }

  print(ans);
}
