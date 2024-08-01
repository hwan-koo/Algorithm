class Solution {
    public int[] solution(int[] array) {
        int index = 0;
        int maxNum = 0;
        for(int i = 0; i < array.length ; i++) {
            if(array[i] > maxNum) {
                maxNum  = array[i];
                index = i;
            }
        }
        int[] answer = {maxNum, index};
        return answer;
    }
}