#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int max_A(string a) {
  if (a[0] != '9') {
    a[0] = '9';
  } else if (a[1] != '9') {
    a[1] = '9';
  } else {
    a[2] = '9';
  }
  return stoi(a);
}

int min_B(string b) {
  if (b[0] != '1') {
    b[0] = '1';
  } else if (b[1] != '0') {
    b[1] = '0';
  } else {
    b[2] = '0';
  }
  return stoi(b);
}

int main() {
  string A, B;
  cin >> A >> B;

  int ans = max(max_A(A) - stoi(B), stoi(A) - min_B(B));
  print(ans);
}
