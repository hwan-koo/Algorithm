class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        char[] originArray = my_string.toCharArray();
        char[] reWriteArray = overwrite_string.toCharArray();
        String answer = "";
        for(int i = 0; i < my_string.length() ; i ++) {
            if ( s <= i  && i < s + overwrite_string.length()) {
                answer += Character.toString(reWriteArray[i-s]);
            } else {
                answer += Character.toString(originArray[i]);
            }
        }
        
        return answer;
    }
}