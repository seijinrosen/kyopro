#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;

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

template <typename T>
T sum(vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

template <typename T>
map<T, int> Counter(vector<T> &vec) {
  map<T, int> counter;
  for (auto &&t : vec) counter[t]++;
  return counter;
}

int main() {
  int N;
  cin >> N;
}
