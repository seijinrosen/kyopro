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

  vector<int> F(N);
  for (auto &&f : F) cin >> f;

  int ans = 0;
  for (auto &&f : F) ans += 1 << f;

  print(ans);
}
