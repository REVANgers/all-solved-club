import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Chapter13_Q17 {

    private static final int[][] MOVE = {
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());

        int s = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        boolean[][] visited = new boolean[n][n];

        int time = 0;

        while (time < s) {
            List<Virus> viruses = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (map[i][j] != 0 && !visited[i][j]) {
                        viruses.add(new Virus(map[i][j], i, j));
                        visited[i][j] = true;
                    }
                }
            }

            Collections.sort(viruses);

            for (Virus virus : viruses) {
                for (int i = 0; i < 4; i++) {
                    int ny = virus.y + MOVE[i][0];
                    int nx = virus.x + MOVE[i][1];

                    if (isInMap(n, ny, nx) && !visited[ny][nx]) {
                        map[ny][nx] = virus.number;
                    }
                }
            }

            time += 1;

            for (int[] line : map) {
                System.out.println(Arrays.toString(line));
            }
        }

        System.out.println(map[y - 1][x - 1]);

        br.close();
    }

    private static boolean isInMap(int n, int y, int x) {
        return ((0 <= y && y < n) && (0 <= x && x < n));
    }
}

class Virus implements Comparable<Virus> {

    int number;
    int y, x;

    public Virus(int number, int y, int x) {
        this.number = number;
        this.y = y;
        this.x = x;
    }

    @Override
    public int compareTo(Virus o) {
        return Integer.compare(o.number, this.number);
    }
}

/*
3 3
1 0 2
0 0 0
3 0 0
2 3 2
 */
