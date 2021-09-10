import java.util.*;

class Solution {
    public static String solution(String[] table, String[] languages, int[] preference) {
        int n = languages.length;
        String answer = "ZZZZZ";
        int max_score = 0;
        for (String str: table) {
            int score = 0;
            String[] split = str.split(" ");
            for (int i = 0; i < n; i++) {
                int index = Arrays.asList(split).indexOf(languages[i]);
                if (index != -1) {
                    score += (6 - index) * preference[i];
                }
            }
            if (score >= max_score) {                
                if (score > max_score) {
                    answer = split[0];
                } else {
                    if (answer.compareTo(split[0]) > 0) {
                        answer = split[0];
                    }
                }
                max_score = score;
            }
        }        
        return answer;
    }
}