#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

int main() {
  int N;
  cin >> N;

  vector<pair<string, string>> ST(N);
  for (auto &&[s, t] : ST) cin >> s >> t;

  set<pair<string, string>> set_ = {ST.begin(), ST.end()};
  bool ans = set_.size() != N;

  print(yes_no(ans));
}
