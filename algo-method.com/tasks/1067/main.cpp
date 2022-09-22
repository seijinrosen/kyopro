#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string reverse(const string &s) { return string(s.rbegin(), s.rend()); }

vector<pair<int, char>> enumerate(const string &s) {
  vector<pair<int, char>> ret(s.size());
  for (size_t i = 0; i < s.size(); i++) ret[i] = {i, s[i]};
  return ret;
}

int bin2int(const string &bin) {
  int ret = 0;
  for (auto &&[i, c] : enumerate(reverse(bin)))
    if (c == '1') ret += 1 << i;
  return ret;
}

int main() {
  int N;
  cin >> N;

  vector<string> vec = {
      "1110111", "0100100", "1011101", "1101101", "0101110",
      "1101011", "1111011", "0100111", "1111111", "1101111",
  };

  int ans = bin2int(vec[N]);
  print(ans);
}
