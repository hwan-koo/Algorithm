import java.util.Arrays;
class Solution {
    public int solution(int[] num_list) {
        if(num_list.length > 10) {
            return Arrays.stream(num_list).sum();
        } else {
            int temp = num_list[0];
            for (int i = 1; i < num_list.length; i++) {
                temp *= num_list[i];
            }
            return temp;
        }
    }
}