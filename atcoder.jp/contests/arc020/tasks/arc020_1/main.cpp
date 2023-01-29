#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  string ans;
  if (abs(A) < abs(B)) {
    ans = "Ant";
  } else if (abs(A) == abs(B)) {
    ans = "Draw";
  } else {
    ans = "Bug";
  }

  cout << ans << endl;
}
