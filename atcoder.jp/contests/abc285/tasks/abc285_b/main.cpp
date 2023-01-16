#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  string S;
  cin >> N >> S;

  for (int i = 1; i < N; i++) {
    int l = 0;

    for (int k = 0; k < N - i; k++) {
      if (S[k] == S[k + i]) break;
      l++;
    }

    cout << l << endl;
  }
}
