#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;

  int ans = (A + B) * (C - D);

  print(ans);
  print("Takahashi");
}
