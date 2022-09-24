#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

template <typename T>
void print(T value) {
  cout << value << endl;
}
template <typename T>
void print(const vector<T> &vec) {
  rep(i, vec.size() - 1) cout << vec.at(i) << " ";
  print(vec.back());
}

void dfs(int v, vector<vector<int>> &G, vector<int> &before) {
  for (auto &&nv : G[v]) {
    if (before[nv] != -1) continue;
    before[nv] = v;
    dfs(nv, G, before);
  }
}

int main() {
  int N, X, Y;
  cin >> N >> X >> Y;

  vector<vector<int>> G(N);
  rep(_, N - 1) {
    int u, v;
    cin >> u >> v;
    G[u - 1].push_back(v - 1);
    G[v - 1].push_back(u - 1);
  }

  vector<int> before(N, -1);
  dfs(X - 1, G, before);

  vector<int> route = {Y - 1};
  while (route.back() != X - 1) route.push_back(before[route.back()]);

  reverse(route.begin(), route.end());
  for (auto &&i : route) i++;

  print(route);
}
