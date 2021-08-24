import java.util.LinkedList;
import java.util.List;

public class Chapter12_Q09 {
    public static void main(String[] args) {
        System.out.println(solution("ababcdcdababcdcd"));
        System.out.println(solution("aabbaccc"));
    }

    public static int solution(String s) {
        int answer = Integer.MAX_VALUE;

        for (int i = 1; i <= s.length(); i++) {
            List<String> substrings = new LinkedList<>();

            for (int j = 0; j < s.length(); j += i) {
                substrings.add(s.substring(j, Math.min(j + i, s.length())));
            }

            substrings.add(""); // end of substrings list.

            StringBuilder sb = new StringBuilder();

            String substring = substrings.get(0);

            int count = 1;

            for (int j = 1; j < substrings.size(); j++) {
                if (substring.equals(substrings.get(j))) {
                    count += 1;
                } else {
                    if (count > 1) {
                        sb.append(count);
                    }

                    sb.append(substring);

                    substring = substrings.get(j);
                    count = 1;
                }
            }

            answer = Math.min(answer, sb.length());
        }

        return answer;
    }
}
