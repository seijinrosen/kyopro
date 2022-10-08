#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

string solve(int n) {
  string fizz = n % 4 == 0 ? "Fizz" : "";
  string buzz = n % 6 == 0 ? "Buzz" : "";
  string ret = fizz + buzz;
  return ret == "" ? to_string(n) : ret;
}

int main() {
  int N;
  cin >> N;

  for (auto &&i : range(1, N + 1)) print(solve(i));
}
