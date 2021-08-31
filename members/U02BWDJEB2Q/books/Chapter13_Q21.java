import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Chapter13_Q21 {

    private static final int[][] Move = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;

        while (true) {
            int[][] union = getUnion(n, l, r, map);

            boolean end = true;

            int max = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (union[i][j] != 0) {
                        max = Math.max(max, union[i][j]);
                        end = false;
                    }
                }
            }

            if (end) {
                break;
            }

            time += 1;

            for (int num = 1; num <= max; num++) {
                int total = 0;
                int count = 0;

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (union[i][j] == num) {
                            total += map[i][j];
                            count += 1;
                        }
                    }
                }

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (union[i][j] == num) {
                            map[i][j] = total / count;
                        }
                    }
                }
            }
        }

        System.out.println(time);

        br.close();
    }

    private static int[][] getUnion(int n, int l, int r, int[][] map) {
        int[][] result = new int[n][n];

        boolean[][] visited = new boolean[n][n];

        int index = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) { // 연합 만들기 시작
                    int current = 0;

                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[]{i, j});
                    visited[i][j] = true;

                    for (int next = 0; next < 4; next++) {
                        int ny = i + Move[next][0];
                        int nx = j + Move[next][1];

                        if (isInMap(n, ny, nx) &&
                                !visited[ny][nx] &&
                                (l <= Math.abs(map[ny][nx] - map[i][j]) && Math.abs(map[ny][nx] - map[i][j]) <= r)) {
                            current = index;
                            break;
                        }
                    }

                    while (!queue.isEmpty()) {
                        int[] p = queue.poll();

                        result[p[0]][p[1]] = current;

                        for (int next = 0; next < 4; next++) {
                            int ny = p[0] + Move[next][0];
                            int nx = p[1] + Move[next][1];

                            if (isInMap(n, ny, nx) &&
                                    !visited[ny][nx] &&
                                    (l <= Math.abs(map[ny][nx] - map[p[0]][p[1]]) && Math.abs(map[ny][nx] - map[p[0]][p[1]]) <= r)) {
                                queue.add(new int[]{ny, nx});
                                visited[ny][nx] = true;
                            }
                        }
                    }

                    if (current != 0) {
                        index += 1;
                    }
                }
            }
        }

        return result;
    }

    private static boolean isInMap(int n, int y, int x) {
        return ((0 <= y && y < n) && (0 <= x && x < n));
    }
}
