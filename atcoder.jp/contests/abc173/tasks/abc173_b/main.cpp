#include <bits/stdc++.h>
using namespace std;

template <typename T>
map<T, int> Counter(vector<T> &vec) {
  map<T, int> counter;
  for (auto &&t : vec) counter[t]++;
  return counter;
}

template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto S = input_vector<string>(N);

  auto counter = Counter(S);
  auto results = {"AC", "WA", "TLE", "RE"};

  for (auto &&r : results) {
    cout << r << " x " << counter[r] << endl;
  }
}
