#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<pair<char, int>> run_length_encoding(const string &str) {
  vector<pair<char, int>> ret = {{str[0], 1}};
  for (auto &&c : str.substr(1)) {
    if (c == ret.back().first)
      ret.back().second++;
    else
      ret.push_back({c, 1});
  }
  return ret;
}

int main() {
  int N;
  string S;
  cin >> N >> S;

  auto run_length = run_length_encoding(S);
  ll ans = 0;

  while (2 <= run_length.size()) {
    auto [_, v] = run_length.back();
    run_length.pop_back();
    run_length.back().second += v + 1;
    ans += v;
  }

  print(ans);
}
