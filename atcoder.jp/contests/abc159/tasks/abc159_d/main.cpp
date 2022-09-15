#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename T>
map<T, int> Counter(vector<T> &vec) {
  map<T, int> counter;
  for (auto &&t : vec) counter[t]++;
  return counter;
}

ll nC2(ll n) {
  if (n < 2) return 0;
  return n * (n - 1) / 2;
}

int main() {
  int N;
  cin >> N;

  vector<int> A(N);
  for (auto &&a : A) cin >> a;

  auto counter = Counter(A);

  ll total = 0;
  for (auto &&[_, v] : counter) total += nC2(v);

  for (auto &&a : A) print(total - nC2(counter[a]) + nC2(counter[a] - 1));
}
