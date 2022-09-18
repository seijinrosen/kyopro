#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

int main() {
  string S;
  cin >> S;

  string ans;

  for (auto &&s : S) {
    if (s == '0' || s == '1') {
      ans += s;
    } else if (s == 'B' && !ans.empty()) {
      ans.pop_back();
    }
  }

  print(ans);
}
