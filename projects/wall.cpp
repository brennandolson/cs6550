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
#define INF 1000000
#define N 2000005

using namespace std;
using ll = long long;
int mode, t;
int wall[N];

struct Node {
  int start, end, opmin, opmax;
  struct Node *left, *right, *parent;
};

struct Node *newNode(int s, int e) {
  struct Node *temp = new Node;
  temp->start = s;
  temp->end = e;
  temp->parent = NULL;
  temp->opmin = INF;
  temp->opmax = 0;
  if (s == e) {
    temp->left = NULL;
    temp->right = NULL;
  } else {
    int m = (s + e) / 2;
    temp->left = newNode(s, m);
    temp->right = newNode(m+1, e);
    temp->left->parent = temp;
    temp->right->parent = temp;
  }
  return temp;
}

class M{//encapsulating two mutually recursive functions
public:

static void minimize(Node & self, int l, int r, int t) {
  if (self.start == l && self.end == r) {
    self.opmin = min(self.opmin, t);
    self.opmax = min(self.opmax, self.opmin);
    return;
  }
  minimize(*self.left, self.left->start, self.left->end, self.opmin);
  maximize(*self.left, self.left->start, self.left->end, self.opmax);
  minimize(*self.right, self.right->start, self.right->end, self.opmin);
  maximize(*self.right, self.right->start, self.right->end, self.opmax);
  self.opmin = INF;
  self.opmax = 0;
  if (r <= self.left->end) {
    minimize(*self.left, l, r, t);
  } else if (l >= self.right->start) {
    minimize(*self.right, l, r, t);
  } else {
    minimize(*self.left, l, self.left->end, t);
    minimize(*self.right, self.right->start, r, t);
  }
}


static void maximize(Node & self, int l, int r, int t) {
  if (self.start == l && self.end == r) {
    self.opmax = max(self.opmax, t);
    self.opmin = max(self.opmax, self.opmin);
    return;
  }
  minimize(*self.left, self.left->start, self.left->end, self.opmin);
  maximize(*self.left, self.left->start, self.left->end, self.opmax);
  minimize(*self.right, self.right->start, self.right->end, self.opmin);
  maximize(*self.right, self.right->start, self.right->end, self.opmax);
  self.opmin = INF;
  self.opmax = 0;
  if (r <= self.left->end) {
    maximize(*self.left, l, r, t);
  } else if (l >= self.right->start) {
    maximize(*self.right, l, r, t);
  } else {
    maximize(*self.left, l, self.left->end, t);
    maximize(*self.right, self.right->start, r, t);
  }
}
};//end mutual recursion encapsulation

int query(Node & self) {
  Node curr = self;
  int val = min(curr.opmin, max(curr.opmax, 0));
  while (curr.parent != NULL) {
    curr = *curr.parent;
    val = min(curr.opmin, max(curr.opmax, val));
  } 
  return val;
}

void get_final(Node & self, int A[]) {
  // cout << "moving down the tree: (start, end) = (" << self.start << ", " << self.end << ")\n";
  if (self.start == self.end) {
    // cout << self.start << " query gives " << query(self) << endl;
    A[self.start] = query(self);
  }
  else {
    get_final(*self.left, A);
    get_final(*self.right, A);
  }
}

void debug(Node &self) {
  cout << "[" << self.start << ", " << self.end << "] min=" << self.opmin << ", max=" << self.opmax << '\n'; 
  if (self.start < self.end) {
    debug(*self.left);
    debug(*self.right);
  }
}

void solve() {
  int n, k;
  cin >> n >> k;
  
  Node *root = newNode(0, n - 1); 
  int c, l, r, v;
  for (int i = 0; i < k; i++) {
    cin >> c >> l >> r >> v;
    if (c == 2) {
      M::minimize(*root, l, r, v);
    } else {
      M::maximize(*root, l, r, v);
    }
  } 

  get_final(*root, wall);
  // debug(*root);
  for (int i = 0; i < n; i++) {
    cout << wall[i] << '\n';
  }
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
