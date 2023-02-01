#include <bits/stdc++.h>
using namespace std;

pair<int, int> func(int x, int y) {
  if (x % 2 == 1) x--;

  int tmp = x / 2;
  x -= tmp;
  y += tmp;

  return {x, y};
}

int main() {
  int a, b, K;
  cin >> a >> b >> K;

  for (size_t i = 0; i < K; i++) {
    if (i % 2 == 0) {
      auto xy = func(a, b);
      a = xy.first;
      b = xy.second;
    } else {
      auto xy = func(b, a);
      b = xy.first;
      a = xy.second;
    }
  }

  cout << a << " " << b << endl;
}
