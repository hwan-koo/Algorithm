import java.util.*;
class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        for(char item : my_string.toCharArray()) {
            String str = Character.toString(item);
            if(str.equals(alp)) {
                answer += str.toUpperCase();
            } else {
                answer += str;
            }
        }
        return answer;
    }
}