#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int N;
  cin >> N;

  int ans = (1 << N) - 1;
  print(ans);
}
