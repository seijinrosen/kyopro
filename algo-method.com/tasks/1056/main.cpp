#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int N, X;
  cin >> N >> X;

  string ans = N & 1 << X ? "Yes" : "No";
  print(ans);
}
