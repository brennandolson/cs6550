#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <numeric>
#include <chrono>

#define fore(i, l, r) for(int i = int(l); i < int(r); i++)
#define sz(a) int((a).size())
#define mp make_pair
#define vi vector<int>
#define vpi vector<pair<int, int>>
#define vl vector<long long>
#define vpl vector<pair<long long, long long>>

using namespace std;
using namespace std::chrono;
using ll = long long;
int mode, t;
ll masks[16][1<<20];
const ll mod = 998244353;
const ll ti = 998243401;

int digsum(int n) {
  int out = 0;
  while (n){
    out += n % 10;
    n /= 10;
  }
  return out;
}

void backtrack(int i, vi &L, int n, int cutoff, vi &counts, vi &xors, int s) {
  if (s == n) { 
    if (*max_element(counts.begin(), counts.end()) < cutoff) return;
    int mask = 0;
    int shift = 1;
    for (int j = 0; j < 5; j++) {
      mask += xors[j] * shift;
      shift <<= 4;
    }
    masks[i][mask]++;
  } else {
    for (int j = 0; j < 5; j++) {
      counts[j]++;
      xors[j] ^= L[s];
      backtrack(i, L, n, cutoff, counts, xors, s + 1);
      counts[j]--;
      xors[j] ^= L[s];
    }
  } 
}

void fwht(int id) {
  int h = 1;
  int n = 1<<20;
  while (h < n) {
    for (int i = 0; i < n; i += h * 2) {
      for (int j = i; j < i + h; j++) {
        ll x = masks[id][j];
        ll y = masks[id][j+h];
        masks[id][j] = (x + y);
        masks[id][j+h] = (x - y);
      }
    }
    h <<= 1;
  }  
  fore (i, 0, n) {
    masks[id][i] %= mod;
  }
}

ll get_score(int m, vl &scores) {
  ll total = 0;
  int i = 0;
  while (m) {
    total += scores[i] * (m&1);
    m >>= 1;
    i = (i + 1) % 4;
  }
  return total;
}

// bisect_right in python
int bis(vl S, ll v) {
  int lo = 0, hi = S.size();
  if (S[0] > v) return 0;
  if (S.back() <= v) return hi;
  int mid;
  while (lo < hi - 1) {
    mid = (lo + hi) / 2;
    if (S[mid] <= v) {
      lo = mid;
    } else {
      hi = mid;
    }
  }
  return hi;
}

void solve() {
  int n; ll q;
  cin >> n >> q;
  vi ghosts;
  string move;
  int voi, bitset;
  unordered_map<string, int> codes = 
  {
    {"spook", 1},
    {"hide", 2},
    {"creep", 4},
    {"float", 8}
  };
  
  // get ghost moves
  fore (i, 0, n) {
    bitset = 0;
    cin >> voi;
    fore(j, 0, voi) {
      cin >> move;
      bitset |= codes[move];
    }
    ghosts.push_back(bitset);
  }
  
  // get score values 
  vl scores(4);
  for (ll &a : scores) cin >> a;
  
  // group the ghosts
  vector<vi> groups(16);
  fore (i, 0, n) {
    groups[digsum(i+1)-1].push_back(ghosts[i]);
  }
  
  // backtracking brute force 
  vi counts(5);
  vi xors(5);

  fore (i, 0, 16) {
    if (groups[i].size() > 0) {
      fore(j, 0, 5) {
        counts[j] = 0;
        xors[j] = 0;
      }
      int n2 = groups[i].size();
      int cutoff = (n2 + 1) >> 1;
      backtrack(i, groups[i], n2, cutoff, counts, xors, 0);
    }
  }

  // walsh-hadamard in place
  // not using sqrt(2)
  // so backing out 
  // 2^20 mod p
  fore (id, 0, 16) {
    if (groups[id].size() > 0) {
      fwht(id);
      if (id > 0) {
        fore(j, 0, 1<<20) {
          masks[0][j] *= masks[id][j];
          masks[0][j] %= mod;
        } 
      }
    }
  }


  fwht(0);
  fore (i, 0, 1<<20) {
    masks[0][i] = (masks[0][i] * ti) % mod;
  }
  

  unordered_map<ll, ll> ways;
  vl S;
  int m = 0;
  fore (i, 0, 1<<20) {
    ll v = masks[0][i];
    if (v != 0) {
      ll g = get_score(i, scores);
      if (ways.count(g) == 0) {
        ways[g] = v;
        S.push_back(g);
        m++;
      } else {
        ways[g] += v;
        // ways[g] %= mod;
      }
    }
  }

  sort(S.begin(), S.end());
  vl partials(m+1);
  fore (i, 0, m) {
    partials[i + 1] = (partials[i] + ways[S[i]]);
  }


  
  // process queries
  int a, b, i, j;
  ll x;
  fore (k, 0, q) {
    cin >> a >> b;
    i = bis(S, a - 1);
    j = bis(S, b);
    x = (partials[j] - partials[i]) % mod;
    if (x >= 0) cout << x << '\n';
    else cout << x + mod << '\n';
  }
}



int main() {
  // auto start = high_resolution_clock::now();
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  mode = 0;
  if (mode == 0) { 
    solve();
  } else {
    cin >> t;
    while (t--) {
      solve();
    }
  }
  // auto stop = high_resolution_clock::now();
  // duration<double> time_span = duration_cast<duration<double>>(stop - start);
  // cout << time_span.count() << " s" << endl;
}
