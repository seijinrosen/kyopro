#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, H, W;
  cin >> N >> H >> W;

  int h = N - H + 1;
  int w = N - W + 1;

  cout << h * w << endl;
}
