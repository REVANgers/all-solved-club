import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Chapter15_Q30 {

    private static final int MAX_LENGTH = 10001;

    public static void main(String[] args) {
        System.out.println(
                Arrays.toString(solution(
                        new String[]{"frodo", "front", "frost", "frozen", "frame", "kakao"},
                        new String[]{"fro??", "????o", "fr???", "fro???", "pro?"}
                ))
        );
    }

    public static int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];

        Trie[] tree = new Trie[MAX_LENGTH];
        Trie[] reverseTree = new Trie[MAX_LENGTH];

        for (int i = 1; i < MAX_LENGTH; i++) {
            tree[i] = new Trie();
            reverseTree[i] = new Trie();
        }

        for (String word : words) {
            tree[word.length()].insert(word);
            reverseTree[word.length()].insert(new StringBuilder(word).reverse().toString());
        }

        for (int i = 0; i < queries.length; i++) {
            String query = queries[i];

            if (query.charAt(0) == '?') {
                answer[i] = reverseTree[query.length()].find(new StringBuilder(query).reverse().toString());
            } else {
                answer[i] = tree[query.length()].find(query);
            }
        }

        return answer;
    }
}

class Trie {

    Node root;

    public Trie() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node current = this.root;

        for (int i = 0; i < word.length(); i++) {
            current.count += 1;
            current = current.children.computeIfAbsent(word.charAt(i), c -> new Node());
        }
    }

    public int find(String query) {
        Node current = this.root;

        for (int i = 0; i < query.length(); i++) {
            if (query.charAt(i) == '?') {
                return current.count;
            }

            current = current.children.get(query.charAt(i));

            if (current == null) {
                return 0;
            }
        }

        return 0;
    }
}

class Node {

    Map<Character, Node> children;
    int count;

    public Node() {
        this.children = new HashMap<>();
        this.count = 0;
    }
}
