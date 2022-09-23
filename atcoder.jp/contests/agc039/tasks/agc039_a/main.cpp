#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<pair<char, int>> count_serial_char(const string &str) {
  vector<pair<char, int>> ret = {{str[0], 1}};
  for (auto &&c : str.substr(1)) {
    if (c == ret.back().first)
      ret.back().second++;
    else
      ret.push_back({c, 1});
  }
  return ret;
}

bool is_odd(int n) { return n % 2 == 1; }

int main() {
  string S;
  int K;
  cin >> S >> K;

  auto counter = count_serial_char(S);

  ll ans = 0;
  for (auto &&[_, v] : counter) ans += v / 2;
  ans *= K;

  if (counter.size() == 1 && is_odd(counter[0].second)) {
    ans += K / 2;
  } else if (counter[0].first == counter.back().first) {
    if (is_odd(counter[0].second) && is_odd(counter.back().second)) {
      ans += K - 1;
    }
  }

  print(ans);
}
