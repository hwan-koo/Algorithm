import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        my_string = my_string.replaceAll("[a-z]", "");
        String[] arr = my_string.split("");
        int size = my_string.length();
        int[] answer = new int[size];
        for(int i = 0 ; i < size; i ++) {
            answer[i] = Integer.parseInt(arr[i]);
        }
        Arrays.sort(answer);
        return answer;
    }
}