#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int int2bin(const string &bin) {
  string reversed = {bin.rbegin(), bin.rend()};
  int ret = 0;
  for (size_t i = 0; i < bin.size(); i++)
    if (reversed[i] == '1') ret += 1 << i;
  return ret;
}

int main() {
  string N;
  cin >> N;

  int ans = int2bin(N);

  print(ans);
}
