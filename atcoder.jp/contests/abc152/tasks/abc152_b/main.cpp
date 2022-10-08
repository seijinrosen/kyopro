#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int ctoi(char c) { return c - '0'; }

int main() {
  char A, B;
  cin >> A >> B;

  string ans = min(string(ctoi(B), A), string(ctoi(A), B));

  print(ans);
}
