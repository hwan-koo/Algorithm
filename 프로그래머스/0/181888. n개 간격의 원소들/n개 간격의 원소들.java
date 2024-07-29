import java.util.*;
class Solution {
    public int[] solution(int[] num_list, int n) {
        ArrayList<Integer> intList = new ArrayList<>();
        for (int i = 0; i < num_list.length ; i++) {
            if (i % n == 0) {
                intList.add(num_list[i]);
            }
        }
        return intList.stream().mapToInt(Integer::intValue).toArray();
    }
}