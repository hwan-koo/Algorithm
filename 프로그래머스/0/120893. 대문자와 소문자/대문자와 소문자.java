class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(char item : my_string.toCharArray()) {
            if(Character.isUpperCase(item)) {
                answer += Character.toString(item).toLowerCase();
            } else{
                answer += Character.toString(item).toUpperCase();
            }
        }
        
        return answer;
    }
}