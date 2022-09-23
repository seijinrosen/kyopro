#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename T>
vector<pair<int, T>> enumerate(const vector<T> &vec) {
  vector<pair<int, T>> ret(vec.size());
  for (size_t i = 0; i < vec.size(); i++) ret[i] = {i, vec[i]};
  return ret;
}

bool startswith(const string &str, const string &prefix) {
  if (str.size() < prefix.size()) return false;
  return str.substr(0, prefix.size()) == prefix;
}

vector<string> tails(const string &str) {
  vector<string> ret(str.size() + 1);
  for (size_t i = 0; i <= str.size(); i++) ret[i] = str.substr(i);
  return ret;
}

int main() {
  int N;
  string S, T;
  cin >> N >> S >> T;

  int ans;
  for (auto &&[i, tail] : enumerate(tails(S))) {
    if (startswith(T, tail)) {
      ans = N + i;
      break;
    }
  }

  print(ans);
}
