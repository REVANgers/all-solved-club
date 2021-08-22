import java.io.*;
import java.util.*;

public class Chapter16_Q32 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<List<Integer>> triangle = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            triangle.add(new ArrayList<>());
        }

        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j <= i; j++) {
                triangle.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                int current = triangle.get(i).get(j);

                int left = j - 1 >= 0 ? current + triangle.get(i - 1).get(j - 1) : current;
                int right = j < i ? current + triangle.get(i - 1).get(j) : current;

                triangle.get(i).set(j, Math.max(left, right));
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                System.out.print(triangle.get(i).get(j) + " ");
            }
            System.out.println();
        }

        int answer = 0;

        for (int i = 0; i < triangle.get(n - 1).size(); i++) {
            answer = Math.max(answer, triangle.get(n - 1).get(i));
        }

        System.out.println(answer);

        br.close();
    }
}

/*
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
 */
