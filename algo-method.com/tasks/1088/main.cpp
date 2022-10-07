#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int SA, TA, SB, TB;
  cin >> SA >> TA >> SB >> TB;

  int ans = max(0, min(TA, TB) - max(SA, SB));

  print(ans);
}
