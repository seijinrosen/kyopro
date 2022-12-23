#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(const vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

int main() {
  int A, B;
  cin >> A >> B;

  vector<int> vec;

  if (A < B) {
    for (int i = 1; i <= B; i++) vec.push_back(-i);
    for (int i = 1; i < A; i++) vec.push_back(i);
  } else {
    for (int i = 1; i <= A; i++) vec.push_back(i);
    for (int i = 1; i < B; i++) vec.push_back(-i);
  }

  vec.push_back(-sum(vec));
  print(vec);
}
