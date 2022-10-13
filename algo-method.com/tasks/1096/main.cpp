#include <bits/stdc++.h>
using namespace std;

vector<string> split(char x, const string &s) {
  vector<string> ret;
  string now = "";
  for (auto &&c : s) {
    if (c == x) {
      ret.push_back(now);
      now = "";
    } else {
      now += c;
    }
  }
  if (!now.empty()) ret.push_back(now);
  return ret;
}

int main() {
  string S;
  cin >> S;

  auto nd = split('/', S);
  int n = stoi(nd[0]);
  int d = stoi(nd[1]);

  int g = gcd(n, d);
  cout << n / g << "/" << d / g << endl;
}
