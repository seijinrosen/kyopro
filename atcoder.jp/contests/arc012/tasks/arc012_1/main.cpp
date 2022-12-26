#include <bits/stdc++.h>
using namespace std;

int solve(const string &day) {
  if (day == "Monday") return 5;
  if (day == "Tuesday") return 4;
  if (day == "Wednesday") return 3;
  if (day == "Thursday") return 2;
  if (day == "Friday") return 1;
  return 0;
}

int main() {
  string day;
  cin >> day;

  cout << solve(day) << endl;
}
