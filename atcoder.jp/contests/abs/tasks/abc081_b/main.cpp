#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
// print functions -------------------------------------------------------------

map<int, int> prime_factorize(int n) {
  map<int, int> counter;
  int p = 2;
  while (p * p <= n) {
    int e = 0;
    while (n % p == 0) {
      e++;
      n /= p;
    }
    if (e != 0) counter[p] = e;
    p++;
  }
  if (n != 1) counter[n] = 1;
  return counter;
}

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);

  int ans = 100;
  for (auto &&a : A) ans = min(ans, prime_factorize(a)[2]);

  print(ans);
}
