import java.util.*;

class Solution {
    public int[] solution(int[] weights, String[] head2head) {
        int len = weights.length;
        int[][] boxers = new int[len][4];
        for (int i = 0; i < len; i++) {
            int win = 0;
            int lose = 0;
            int fat_win = 0;
            for (int j = 0; j < len; j++) {
                if (head2head[i].charAt(j) == 'W') {
                    win++;
                    if (weights[i] < weights[j]) {
                        fat_win++;
                    }
                } else if (head2head[i].charAt(j) == 'L') {
                    lose++;
                }
            }
            int win_rate = 0;
            if (win > 0) {
                win_rate = (int)((double)win / (win + lose) * 10000000);
            }            
            boxers[i][0] = win_rate;
            boxers[i][1] = fat_win;
            boxers[i][2] = weights[i];
            boxers[i][3] = i + 1;
        }
        Arrays.sort(boxers, (a, b) -> {
            if (a[0] != b[0]) return a[0] > b[0] ? -1 : 1;
            if (a[1] != b[1]) return a[1] > b[1] ? -1 : 1;
            if (a[2] != b[2]) return a[2] > b[2] ? -1 : 1;
            return a[3] < b[3] ? -1 : 1;
        });
        int[] answer = new int[len];
        for (int i = 0; i < len; i++) {
            answer[i] = boxers[i][3];
        }
        return answer;
    }
}
