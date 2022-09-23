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

char get_square(const string &bin_x, int j) {
  if (bin_x[2 * j] == '0' && bin_x[2 * j + 1] == '0') return '.';
  if (bin_x[2 * j] == '0' && bin_x[2 * j + 1] == '1') return 'o';
  return 'x';
}

string get_line(int x) {
  string bin_x = int2bin(x, 16);
  string ret;
  for (size_t j = 0; j < 8; j++) ret += get_square(bin_x, j);
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  auto X = input_vector(8);
  for (auto &&x : X) print(get_line(x));
}
