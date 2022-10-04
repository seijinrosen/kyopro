#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

bool is_odd(int n) { return n % 2 == 1; }

int main() {
  int A, B;
  cin >> A >> B;

  string ans = is_odd(A * B) ? "Odd" : "Even";
  print(ans);
}
