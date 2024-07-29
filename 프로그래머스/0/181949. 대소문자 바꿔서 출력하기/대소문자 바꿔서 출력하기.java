import java.util.Scanner;


public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer = "";
        String a = sc.next();
        for(char item : a.toCharArray()) {
            if(Character.isLowerCase(item)) {
                answer += Character.toString(item).toUpperCase();
            } else {
                answer += Character.toString(item).toLowerCase();
            }
        }
        System.out.println(answer);
    }
}