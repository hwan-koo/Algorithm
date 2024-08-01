import java.util.*;
class Solution {
    public String solution(String my_string) {
        char[] stringList = my_string.toCharArray();
        List<String> answerList = new ArrayList<>(); 
        for(char item : stringList) {
            String inputValue =Character.toString(item) ;
            if(answerList.contains(inputValue)) {
                continue;
            } else{
                answerList.add(inputValue);
            }
        }
        String answer = String.join("", answerList);
        return answer;
    }
}