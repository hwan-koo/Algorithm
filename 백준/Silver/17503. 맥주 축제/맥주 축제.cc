#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
 
using namespace std;
 
typedef long long ll;
typedef pair<ll, ll> cl;
 
const long long MAX_SUGAR =1e13;
 
bool compare(cl juice1, cl juice2){return juice1.second < juice2.second;}
 
ll maxPreferSum(ll n, vector<cl> juices, ll sugar){
  vector<ll> drinking;
  ll sum =0;
 
  for (int i =0; i < juices.size(); i++){
    if (juices[i].second > sugar)
      break;
    drinking.push_back(juices[i].first);
  }
 
  if (drinking.size()< n)
    return -1;
 
  sort(drinking.begin(), drinking.end(), greater<ll>());
 
  for (int i =0; i < n; i++)
    sum += drinking[i];
 
  return sum;
}
 
ll binarySearch(ll n, ll m, ll k, vector<cl> juices, ll left, ll right){
  ll ans = MAX_SUGAR;
  while (left <= right){
    ll mid =(left + right)/2;
    if (maxPreferSum(n, juices, mid)< m){
      left = mid +1;
    }else {
      right = mid -1;
      ans = min(ans, mid);
      }
  }
  return ans == MAX_SUGAR ?-1 : ans;
}
 
int main(){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
 
  ll n, m, k;
 
  cin >> n >> m >> k;
 
  vector<cl> juices(k);
 
  for (int i =0; i < k; i++){
    cin >> juices[i].first >> juices[i].second;
  }
 
  sort(juices.begin(), juices.end(), compare);
 
  cout << binarySearch(n, m, k, juices, 1, MAX_SUGAR);
}