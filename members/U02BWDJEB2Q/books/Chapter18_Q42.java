import java.io.*;
import java.util.*;

public class Chapter18_Q42 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int g = Integer.parseInt(br.readLine());
        int p = Integer.parseInt(br.readLine());

        int[] planes = new int[p];

        for (int i = 0; i < p; i++) {
            planes[i] = Integer.parseInt(br.readLine());
        }

        int[] stations = new int[g + 1];

        for (int i = 1; i <= g; i++) {
            stations[i] = i;
        }

        int answer = 0;

        for (int i = 0; i < p; i++) {
            int plane = planes[i];

            int gate = getParent(stations, plane);

            if (gate == 0) {
                break;
            } else {
                union(stations, gate, gate - 1);
            }

            answer += 1;
        }

        System.out.println(answer);

        br.close();
    }

    private static int getParent(int[] parent, int x) {
        if (parent[x] == x) {
            return x;
        }

        return parent[x] = getParent(parent, parent[x]);
    }

    private static boolean find(int[] parent, int a, int b) {
        a = getParent(parent, a);
        b = getParent(parent, b);

        return a == b;
    }

    private static void union(int[] parent, int a, int b) {
        a = getParent(parent, a);
        b = getParent(parent, b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }
}