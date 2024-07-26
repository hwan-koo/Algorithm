import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> a = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            for(int j = 0; j < arr[i] ; j++) {
                a.add(arr[i]);
            };
        };
        int[] answer = new int[a.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = a.get(i);
        }
        
        return answer;
    }
    }
