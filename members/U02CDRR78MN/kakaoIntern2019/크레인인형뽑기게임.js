// 회전을 사용하지 않아도 돼서 재풀이
function solution(board, moves) {
  const stack = [];

  return moves.reduce((acc, m) => {
    for (let y = 0; y < board.length; y++) {
      if (board[y][m - 1]) {
        if (stack[stack.length - 1] === board[y][m - 1]) {
          stack.pop();
          acc += 2;
        } else {
          stack.push(board[y][m - 1]);
        }

        board[y][m - 1] = 0;
        return acc;
      }
    }
    return acc;
  }, 0);
}

// 회전 이용
function solution(board, moves) {
  const rotated = board.map((row, r) =>
    row.map((b, c) => board[c][board.length - 1 - r])
  );
  const stack = [];

  return moves.reduce((acc, m) => {
    const row = rotated[rotated.length - m];

    const picked = row.findIndex((d) => d);
    if (picked === -1) return acc;

    if (stack[stack.length - 1] === row[picked]) {
      stack.pop();
      acc += 2;
    } else {
      stack.push(row[picked]);
    }

    row[picked] = 0;

    return acc;
  }, 0);
}
