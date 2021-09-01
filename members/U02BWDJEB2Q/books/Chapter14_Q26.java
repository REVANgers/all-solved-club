import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Chapter14_Q26 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            pq.add(Integer.parseInt(br.readLine()));
        }

        int answer = 0;

        while (pq.size() > 1) {
            int a = pq.poll();
            int b = pq.poll();

            answer += (a + b);

            pq.add(a + b);
        }

        System.out.println(answer);

        br.close();
    }
}
