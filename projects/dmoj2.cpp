#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <numeric>
#include <math.h>

#define fore(i, l, r) for(int i = int(l); i < int(r); i++)
#define sz(a) int((a).size())
#define mp make_pair
#define vi vector<int>
#define vpi vector<pair<int, int>>
#define vl vector<long long>
#define vpl vector<pair<long long, long long>>
#define SIEVE_MAX 1000000

using namespace std;
using ll = long long;
int mode, t;

ll sieve[SIEVE_MAX + 1];
void fillSieve() {
  fore(i, 0, SIEVE_MAX + 1) {
    sieve[i] = i;
  }

  for (ll i = 2; i <= SIEVE_MAX; i++) {
    if (sieve[i] == i) {
      for (ll j = i; j <= SIEVE_MAX; j+= i) {
        sieve[j] -= sieve[j] / i;
      }
    }
  }
}

ll phi(ll n) {
  if (n <= SIEVE_MAX) {
    return sieve[n];
  }

  ll result = n;
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
      while (n % i == 0) {
        n /= i;
      }
      result -= result / i;
    }
  }

  if (n > 1) {
    result -= result / n;
  }
  return result;
}
 
ll pow(ll a, ll b, ll m) {
  ll res = 1;

  a %= m;
  while (b > 0) {
    if (b&1) res = (res * a) % m;

    a = (a * a) % m;
    b >>= 1;
  }
  return res;
}

ll tower(vl &A, int i, ll m) {
  if (i == A.size() - 1) return A[i] % m;
  ll tot = phi(m);
  ll b = tower(A, i + 1, tot);
  return pow(A[i], b + tot, m);
}

void solve() {
  ll n, m;
  cin >> n >> m;

  vl A;
  ll a;
  bool oneSeen = false;
  fore (i, 0, n) {
    cin >> a;
    if (!oneSeen) {
      if (a == 1) oneSeen = true;
      else A.push_back(a);
    }
  }

  // first int was 1
  if (A.size() == 0) {
    cout << 1 << endl;
    return;
  }

  // avoiding gcd problems
  // when power tower has small values
  // calculate by hand. 
  // Later, when all powers are big,
  // we can be sure that a^(x...) 
  // is at least phi(y)
  ll b;
  double al;
  while (A.size() > 1) {
    b = A.back(); A.pop_back();
    a = A.back(); A.pop_back();
    al = log10((double) a);
    if ((double) b * al < 9) {
      A.push_back(pow(a, b, 1e9));
    } else {
      A.push_back(a);
      A.push_back(b);
      break;
    }
  }

  if (A.size() == 1) {
    cout << A[0] % m << endl;
    return;
  }


  // Sieving for phi(n) up to 1M or so.
  // Faster to do this as far as memory will
  // allow, and then use sqrt(n) time algo
  // above the cutoff
  fillSieve();

  ll ans = tower(A, 0, m);
  cout << ans << endl;
}



int main() {
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
}
