import java.util.*;
class Solution {
    public String[] solution(String[] strArr) {
        ArrayList<String> strList = new ArrayList<>();
        for(int i = 0; i < strArr.length ; i++) {
            if(i % 2 == 0) {
                strList.add(strArr[i].toLowerCase());
            } else {
                strList.add(strArr[i].toUpperCase());
            }
        }
        String[] answer = strList.toArray(new String[0]);
        return answer;
    }
}