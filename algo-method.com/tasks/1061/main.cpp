#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  int A, M;
  cin >> A >> M;

  string ans = A & M ? "Yes" : "No";
  print(ans);
}
