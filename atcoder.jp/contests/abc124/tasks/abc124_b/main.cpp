#include <bits/stdc++.h>
using namespace std;

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto H = input_vector(N);

  int current = 0;
  int ans = 0;

  for (auto &&h : H) {
    if (current <= h) {
      current = h;
      ans++;
    }
  }

  cout << ans << endl;
}
