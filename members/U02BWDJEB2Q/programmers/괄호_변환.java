package programmers;

import java.util.Stack;

public class 괄호_변환 {

    public static void main(String[] args) {
        System.out.println(solution("(()())()"));
        System.out.println(solution(")("));
        System.out.println(solution("()))((()"));
    }

    public static String solution(String p) {
        if (p.length() == 0) {
            return "";
        }

        int countOfLeft = 0;
        int countOfRight = 0;

        int i;

        for (i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                countOfLeft += 1;
            } else {
                countOfRight += 1;
            }

            if (countOfLeft == countOfRight) {
                break;
            }
        }

        String u = p.substring(0, i + 1);
        String v = i + 1 < p.length() ? p.substring(i + 1) : "";

        if (isCorrect(u)) {
            u += solution(v);
        }

        if (!isCorrect(u)) {
            StringBuilder result = new StringBuilder("(");

            result.append(solution(v));

            result.append(")");

            u = u.substring(1, u.length() - 1);

            for (i = 0; i < u.length(); i++) {
                result.append(u.charAt(i) == '(' ? ')' : '(');
            }

            return result.toString();
        }

        return u;
    }

    private static boolean isCorrect(String u) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < u.length(); i++) {
            char c = u.charAt(i);

            if (c == '(') {
                stack.push(c);
            } else {
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }

        return stack.isEmpty();
    }
}
