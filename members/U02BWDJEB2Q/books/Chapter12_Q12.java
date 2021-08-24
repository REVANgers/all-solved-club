import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Chapter12_Q12 {

    public static void main(String[] args) {
        int[][] buildFrame = {
                {1, 0, 0, 1}, {1, 1, 1, 1}, {2, 1, 0, 1}, {2, 2, 1, 1},
                {5, 0, 0, 1}, {5, 1, 0, 1}, {4, 2, 1, 1}, {3, 2, 1, 1}
        };

        System.out.println(Arrays.deepToString(solution(5, buildFrame)));
    }

    public static int[][] solution(int n, int[][] buildFrame) {
        List<int[]> structures = new ArrayList<>();

        for (int[] frame : buildFrame) {
            int x = frame[0];
            int y = frame[1];
            int a = frame[2]; // 0 : 기둥, 1 : 보
            int b = frame[3];

            if (b == 0) { // 삭제
                int[] removed = new int[3];

                for (int i = 0; i < structures.size(); i++) {
                    int[] current = structures.get(i);

                    if (current[0] == x && current[1] == y && current[2] == a) {
                        removed = structures.remove(i);
                        break;
                    }
                }

                if (!isPossible(structures)) {
                    structures.add(removed);
                }
            } else if (b == 1) { // 설치
                structures.add(new int[]{x, y, a});

                if (!isPossible(structures)) {
                    for (int i = 0; i < structures.size(); i++) {
                        int[] current = structures.get(i);

                        if (current[0] == x && current[1] == y && current[2] == a) {
                            structures.remove(i);
                            break;
                        }
                    }
                }
            }
        }

        structures.sort((o1, o2) -> {
            if (o1[0] == o2[0]) {
                if (o1[1] == o2[1]) {
                    return Integer.compare(o1[2], o2[2]);
                }

                return Integer.compare(o1[1], o2[1]);
            }

            return Integer.compare(o1[0], o2[0]);
        });

        return structures.toArray(new int[0][0]);
    }

    public static boolean isPossible(List<int[]> structures) {
        for (int[] structure : structures) {
            int x = structure[0];
            int y = structure[1];
            int a = structure[2];

            if (a == 0) { // 기둥
                boolean isGround = (y == 0);

                boolean onPillar = false;
                for (int[] other : structures) {
                    if (other[2] == 0 &&
                            other[0] == x && other[1] == y - 1) {
                        onPillar = true;
                        break;
                    }
                }

                boolean onFloor = false;
                for (int[] other : structures) {
                    if (other[2] == 1 &&
                            ((other[0] == x - 1 && other[1] == y) || (other[0] == x && other[1] == y))) {
                        onFloor = true;
                        break;
                    }
                }

                if (isGround || onPillar || onFloor) {
                    continue;
                }

                return false;
            } else if (a == 1) { // 보
                boolean onPillar = false;
                for (int[] other : structures) {
                    if (other[2] == 0 &&
                            ((other[0] == x && other[1] == y - 1) || (other[0] == x + 1 && other[1] == y - 1))) {
                        onPillar = true;
                        break;
                    }
                }

                int floorCount = 0;
                for (int[] other : structures) {
                    if (other[2] == 1 &&
                            ((other[0] == x - 1 && other[1] == y) || (other[0] == x + 1 && other[1] == y))) {
                        floorCount += 1;
                    }
                }

                if (onPillar || floorCount == 2) {
                    continue;
                }

                return false;
            }
        }

        return true;
    }
}
