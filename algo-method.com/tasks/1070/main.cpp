#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int ctoi(char c) { return c - '0'; }

string yes_no(bool b) { return b ? "Yes" : "No"; }

int main() {
  string X;
  char P, Q;
  cin >> X >> P >> Q;

  map<char, int> user = {{'o', 0}, {'g', 1}, {'u', 2}};
  map<char, int> permission = {{'r', 4}, {'w', 2}, {'x', 1}};

  bool ans = ctoi(X[user[P]]) & permission[Q];
  print(yes_no(ans));
}
