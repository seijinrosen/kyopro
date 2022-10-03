#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

const string ascii_lowercase = "abcdefghijklmnopqrstuvwxyz";

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  auto P = input_vector(26);

  string ans = "";
  for (auto &&p : P) ans += ascii_lowercase[p - 1];

  print(ans);
}
