#include <bits/stdc++.h>
using namespace std;

// input functions -------------------------------------------------------------
using Tuple = tuple<int, int, int, int>;
vector<Tuple> input_tuple_vector(int n) {
  vector<Tuple> ret(n);
  for (auto &&[a, b, c, d] : ret) cin >> a >> b >> c >> d;
  return ret;
}
// input functions -------------------------------------------------------------

int subtract_break_time(int m) {
  if (m <= 360) return m;
  if (m <= 480) return m - 45;
  return m - 60;
}

int func(Tuple info) {
  auto [sh, sm, eh, em] = info;
  return subtract_break_time(60 * (eh - sh) + em - sm);
}

int main() {
  auto INFO = input_tuple_vector(30);

  int totalMinutes = 0;
  for (auto &&info : INFO) totalMinutes += func(info);

  int h = totalMinutes / 60;
  int m = totalMinutes % 60;

  cout << h << " " << m << endl;
}
