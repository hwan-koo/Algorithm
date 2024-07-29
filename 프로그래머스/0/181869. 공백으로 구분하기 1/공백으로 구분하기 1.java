import java.util.ArrayList;
class Solution {
    public String[] solution(String my_string) {
        String[] splitiedArray = my_string.split(" ");
        ArrayList<String> AnswerList = new ArrayList<>();
        for(String item : splitiedArray) {
        if(!item.equals("")) {
            AnswerList.add(item);
        }
        }
        String[] answer = AnswerList.toArray(new String[0]);
        return answer;
    }
}