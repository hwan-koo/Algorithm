class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        String[] temp = cipher.split("");
        for(int i = 1 ; i < cipher.length() + 1; i++){
            if( i % code == 0) {
                answer += temp[i - 1];
            }
            
        }
        return answer;
    }
}