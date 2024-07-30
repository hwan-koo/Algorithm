class Solution {
    public int solution(int a, int b) {
        int left = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int right = Integer.parseInt(Integer.toString(b) + Integer.toString(a));
        if(left > right) {
            return left;
        } else {
            return right;
        }
        
    }
}