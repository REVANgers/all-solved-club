class Solution {
    public String solution(int[][] scores) {
        String answer = "";
        int n = scores.length;
        for (int j = 0; j < n; j++) {
            int total = 0, max = 0, max_count = 0, min = 100, min_count = 0;
            for (int i = 0; i < n; i++) {
                total += scores[i][j];
                if (scores[i][j] >= max) {
                    if (scores[i][j] == max) max_count++;
                    else max_count = 0;
                    max = scores[i][j];
                }
                if (scores[i][j] <= min) {
                    if (scores[i][j] == min) min_count++;
                    else min_count = 0;
                    min = scores[i][j];
                }
            }
            if ((scores[j][j] == max && max_count == 0) || (scores[j][j] == min && min_count == 0)) answer += grade((double) (total - scores[j][j]) / (n - 1));
            else answer += grade((double) total / n);
        }
            return answer;
    }

    static char grade(double score) {
        if (score < 50) return 'F';
        if (score < 70) return 'D';
        if (score < 80) return 'C';
        if (score < 90) return 'B';
        return 'A';
    }
}
