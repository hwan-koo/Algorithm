class Solution {
    public String solution(String myString) {
        String answer = "";
        char[] charArray = myString.toCharArray();
        for (char item : charArray) {
            String temp = Character.toString(item);
            if(temp.equals("a")) {
                answer += "A";
            } else {
                if(!temp.equals("A") && Character.isUpperCase(item)) {
                    answer += temp.toLowerCase();
                } else {
                    answer += temp;
                }
            }
        }
        return answer;
    }
}