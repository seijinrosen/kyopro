#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string reverse(const string &s) { return {s.rbegin(), s.rend()}; }
bool is_prefix(const string &prefix, const string &s) {
  if (s.size() < prefix.size()) return false;
  return s.substr(0, prefix.size()) == prefix;
}
string yes_no(bool b) { return b ? "YES" : "NO"; }

vector<string> candidates = {"dream", "dreamer", "erase", "eraser"};

bool solve(const string &s) {
  string now = s;
  while (!now.empty()) {
    auto prefix = find_if(candidates.begin(), candidates.end(),
                          [&](const string &p) { return is_prefix(p, now); });
    if (prefix == candidates.end()) return false;
    now = now.substr((*prefix).size());
  }
  return true;
}

int main() {
  string S;
  cin >> S;

  for (auto &&s : candidates) s = reverse(s);
  bool ans = solve(reverse(S));

  print(yes_no(ans));
}
