class Solution {
    public int solution(String s) {
        String[] stringList = s.split(" ");
        int beforeValue = Integer.parseInt(stringList[0]);
        int answer = beforeValue;
        for(int i = 1; i < stringList.length; i ++) {
            if(stringList[i].equals("Z")) {
                answer -= beforeValue;
            } else {
                beforeValue = Integer.parseInt(stringList[i]);
                answer += Integer.parseInt(stringList[i]);
            }
        }
        
        return answer;
    }
}