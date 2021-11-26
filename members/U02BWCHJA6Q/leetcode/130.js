/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function (board) {
  const visited = Array.from(Array(board.length), () =>
    Array(board[0].length).fill(false),
  );
  const bfs = (y, x) => {
    visited[y][x] = true;
    if (board[y][x] === 'X') {
      return;
    }

    const dy = [1, -1, 0, 0];
    const dx = [0, 0, -1, 1];
    const q = [{ y, x }];
    board[y][x] = 1;

    while (q.length > 0) {
      const { y, x } = q.shift();

      for (let i = 0; i < 4; i++) {
        const nextY = y + dy[i];
        const nextX = x + dx[i];

        if (
          nextY < 0 ||
          nextY >= board.length ||
          nextX < 0 ||
          nextX >= board[0].length
        ) {
          continue;
        }
        if (visited[nextY][nextX]) {
          continue;
        }
        if (board[nextY][nextX] === 'X') {
          continue;
        }
        console.log(y, x, nextY, nextX);

        visited[nextY][nextX] = true;
        board[nextY][nextX] = 1;
        q.push({ y: nextY, x: nextX });
      }
    }
  };

  for (let y = 0; y < board.length; y++) {
    bfs(y, 0);
    bfs(y, board[0].length - 1);
  }

  for (let x = 0; x < board[0].length; x++) {
    bfs(0, x);
    bfs(board.length - 1, x);
  }

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      if (board[y][x] === 1) {
        board[y][x] = 'O';

        continue;
      }

      if (board[y][x] === 'O') {
        board[y][x] = 'X';
      }
    }
  }

  return board;
};
