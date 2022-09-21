#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

int main() {
  int A, M;
  cin >> A >> M;

  bool ans = (A & M) == M;
  print(yes_no(ans));
}
