#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<string> S(N);
  for (auto &&s : S) cin >> s;

  bool ans = N / 2 < count(S.begin(), S.end(), "For");

  cout << (ans ? "Yes" : "No") << endl;
}
