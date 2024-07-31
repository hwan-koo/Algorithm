import java.util.*;
class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        Arrays.sort(array);
        for (int item : array) {
            if(item > height) {
                return array.length - answer;
            } else {
                answer += 1;
            }
        }
        return array.length - answer;
        
    }
}