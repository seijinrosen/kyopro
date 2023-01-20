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
  auto P = input_vector(N);

  int cnt = 0;
  for (int i = 0; i < N; i++)
    if (i + 1 != P[i]) cnt++;

  bool ans = cnt == 0 || cnt == 2;

  cout << (ans ? "YES" : "NO") << endl;
}
