import java.io.*;
import java.util.*;

public class Chapter15_Q28 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] array = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(n, array);

        System.out.println(answer);

        br.close();
    }

    private static int solution(int n, int[] array) {
        int start = 0;
        int end = n - 1;

        int result = -1; // There is no fixed point.

        while (start <= end) {
            int mid = (start + end) / 2;

            if (array[mid] == mid) {
                result = mid;
                break;
            } else if (array[mid] > mid) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return result;
    }
}