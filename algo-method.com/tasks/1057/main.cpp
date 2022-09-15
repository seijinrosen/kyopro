#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

template <typename T>
void print(T value) {
  cout << value << endl;
}
template <typename T>
void print(vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (int i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

int main() {
  int N;
  cin >> N;

  vector<int> ans;
  rep(i, 30) if (N & 1 << i) ans.push_back(i);

  print(ans.size());
  print(ans);
}
