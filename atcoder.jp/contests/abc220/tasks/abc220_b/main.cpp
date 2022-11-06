#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll read_int_at_base(int base, const string &s) {
  ll ret = 0;
  for (auto &&c : s) ret = ret * base + c - '0';
  return ret;
}

int main() {
  int K;
  string A, B;
  cin >> K >> A >> B;

  ll ans = read_int_at_base(K, A) * read_int_at_base(K, B);
  cout << ans << endl;
}
