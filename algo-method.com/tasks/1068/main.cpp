#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int bin2int(const string &bin) {
  string reversed = {bin.rbegin(), bin.rend()};
  int ret = 0;
  for (size_t i = 0; i < bin.size(); i++)
    if (reversed[i] == '1') ret += 1 << i;
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;

  vector<string> vec = {
      "1110111", "0100100", "1011101", "1101101", "0101110",
      "1101011", "1111011", "0100111", "1111111", "1101111",
  };

  int ans = bin2int(vec[N]) ^ bin2int(vec[M]);
  print(ans);
}
