function solution(board) {
  const size = board.length;
  const stack = [[[0, 0], "h", 0]];
  const visited = {
    h: Array(size)
      .fill(0)
      .map((_) => Array(size).fill(0)),
    v: Array(size)
      .fill(0)
      .map((_) => Array(size).fill(0)),
  };

  while (stack.length) {
    const [[x, y], dir, time] = stack.shift();

    if (
      [dir, x, y].join(",") === `h,${size - 2},${size - 1}` ||
      [dir, x, y].join(",") === `v,${size - 1},${size - 2}`
    ) {
      return time;
    }

    if (visited[dir][y][x]) {
      continue;
    }
    visited[dir][y][x] = 1;

    if (dir === "h") {
      // 좌우상하
      if (board[y][x - 1] === 0) {
        stack.push([[x - 1, y], "h", time + 1]);
      }
      if (board[y][x + 2] === 0) {
        stack.push([[x + 1, y], "h", time + 1]);
      }
      if (y - 1 >= 0 && board[y - 1][x] === 0 && board[y - 1][x + 1] === 0) {
        stack.push([[x, y - 1], "h", time + 1]);
        // 회전
        stack.push([[x, y - 1], "v", time + 1]);
        stack.push([[x + 1, y - 1], "v", time + 1]);
      }
      if (y + 1 < size && board[y + 1][x] === 0 && board[y + 1][x + 1] === 0) {
        stack.push([[x, y + 1], "h", time + 1]);
        // 회전
        stack.push([[x, y], "v", time + 1]);
        stack.push([[x + 1, y], "v", time + 1]);
      }
    }

    if (dir === "v") {
      // 좌우상하
      if (board[y][x - 1] === 0 && board[y + 1][x - 1] === 0) {
        stack.push([[x - 1, y], "v", time + 1]);
        // 회전
        stack.push([[x - 1, y], "h", time + 1]);
        stack.push([[x - 1, y + 1], "h", time + 1]);
      }
      if (board[y][x + 1] === 0 && board[y + 1][x + 1] === 0) {
        stack.push([[x + 1, y], "v", time + 1]);
        // 회전
        stack.push([[x, y], "h", time + 1]);
        stack.push([[x, y + 1], "h", time + 1]);
      }
      if (y - 1 >= 0 && board[y - 1][x] === 0) {
        stack.push([[x, y - 1], "v", time + 1]);
      }
      if (y + 2 < size && board[y + 2][x] === 0) {
        stack.push([[x, y + 1], "v", time + 1]);
      }
    }
  }
}
