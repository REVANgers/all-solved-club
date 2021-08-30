import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Chapter13_Q19 {

    private static int MAX = Integer.MIN_VALUE;
    private static int MIN = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] a = getArray(br);

        int[] ops = getOperations(br);

        dfs(a, ops, 1, a[0]);

        printAnswer();

        br.close();
    }

    private static void printAnswer() {
        System.out.println(MAX);
        System.out.println(MIN);
    }

    private static int[] getOperations(BufferedReader br) throws IOException {
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int[] ops = new int[4];

        for (int i = 0; i < 4; i++) {
            ops[i] = Integer.parseInt(st.nextToken());
        }
        return ops;
    }

    private static int[] getArray(BufferedReader br) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int[] a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        return a;
    }

    private static void dfs(int[] a, int[] ops, int index, int result) {
        if (index == a.length) {
            MAX = Math.max(MAX, result);
            MIN = Math.min(MIN, result);
            return;
        }

        // 0: + | 1: - | 2: * | 3: /
        for (int i = 0; i < 4; i++) {
            if (ops[i] != 0) {
                ops[i] -= 1;

                int next = result;
                int operand = a[index];

                if (i == 0) {
                    next = next + operand;
                } else if (i == 1) {
                    next = next - operand;
                } else if (i == 2) {
                    next = next * operand;
                } else {
                    if (next < 0) {
                        next = -(Math.abs(next) / operand);
                    } else {
                        next = next / operand;
                    }
                }

                dfs(a, ops, index + 1, next);

                ops[i] += 1; // back tracking
            }
        }
    }
}
