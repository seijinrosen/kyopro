#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int X;
  cin >> X;

  int coin500 = X / 500;
  int coin5 = X % 500 / 5;

  int ans = 1000 * coin500 + 5 * coin5;
  print(ans);
}
