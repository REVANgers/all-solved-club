function solution(board, aloc, bloc) {
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, -1, 1];
  const OFF = 0;
  const ON = 1;

  const isPossiblePosition = (y, x) =>
    y >= 0 && y < board.length && x >= 0 && x < board[0].length;

  const isFinished = ([y, x]) => {
    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (isPossiblePosition(nextY, nextX) && board[nextY][nextX] === ON) {
        return false;
      }
    }

    return true;
  };

  const dfs = (aloc, bloc) => {
    if (isFinished(aloc)) {
      return { win: false, turn: 0 };
    }
    if (aloc[0] === bloc[0] && aloc[1] === bloc[1]) {
      return { win: true, turn: 1 };
    }

    let canWin = false;
    let minTurn = Infinity;
    let maxTurn = 0;
    const [y, x] = aloc;

    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (!isPossiblePosition(nextY, nextX) || board[nextY][nextX] === OFF) {
        continue;
      }

      board[y][x] = OFF;
      const { win, turn } = dfs(bloc, [nextY, nextX]);
      board[y][x] = ON;

      if (!win) {
        canWin = true;
        minTurn = Math.min(minTurn, turn);
      } else if (!canWin) {
        maxTurn = Math.max(maxTurn, turn);
      }
    }

    return { win: canWin, turn: 1 + (canWin ? minTurn : maxTurn) };
  };

  return dfs(aloc, bloc).turn;
}
