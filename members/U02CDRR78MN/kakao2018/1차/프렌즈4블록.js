function solution(m, n, board) {
  var answer = 0;

  let rotated = Array(n)
    .fill(0)
    .map((col) => Array(m).fill(0));

  board.forEach((col, c) =>
    col.split("").forEach((block, r) => {
      rotated[r][m - 1 - c] = block;
    })
  );

  while (true) {
    let removed = 0;
    let marked = rotated.map((col) => [...col]);

    rotated.slice(0, -1).forEach((col, c) =>
      col.slice(0, -1).forEach((block, r) => {
        if (
          rotated[c].slice(r, r + 2).join("") +
            rotated[c + 1].slice(r, r + 2).join("") ===
          block.repeat(4)
        ) {
          marked[c][r] = "";
          marked[c][r + 1] = "";
          marked[c + 1][r + 1] = "";
          marked[c + 1][r] = "";
        }
      })
    );

    rotated = marked.map((col) => {
      const filtered = col.filter((block) => block !== "");
      removed += col.length - filtered.length;

      return filtered;
    });

    answer += removed;

    if (removed === 0) {
      return answer;
    }
  }
}
