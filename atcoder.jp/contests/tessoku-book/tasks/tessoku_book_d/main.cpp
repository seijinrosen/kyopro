#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string int2bin(int number, int width) {
  string ret(width, '0');
  for (size_t i = 0; i < width; i++)
    if (number & 1 << i) ret[i] = '1';
  return {ret.rbegin(), ret.rend()};
}

int main() {
  int N;
  cin >> N;

  string ans = int2bin(N, 10);

  print(ans);
}
