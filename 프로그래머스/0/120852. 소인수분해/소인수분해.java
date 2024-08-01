import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> intList = new ArrayList<>();
        int index = 2;
        while(index <= n) {
            if(n % index == 0) {
                if(!intList.contains(index)){
                    intList.add(index);
                }
                n = n / index;
                index = 2;
                
            } else {
                index ++;
            }
        }
        return intList.stream().mapToInt(i -> i).toArray();
    }
}