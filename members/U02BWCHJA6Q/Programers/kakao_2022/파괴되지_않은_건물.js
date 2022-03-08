function solution(board, skill) {
  const TYPE = {
    ATTACK: 1,
    DEFENCE: 2,
  };

  const sumBoard = Array.from(Array(board.length + 1), () =>
    Array(board[0].length + 1).fill(0)
  );

  skill.forEach(([type, r1, c1, r2, c2, degree]) => {
    const resultDegree = type === TYPE.ATTACK ? -degree : degree;

    sumBoard[r1][c1] += resultDegree;
    sumBoard[r2 + 1][c1] -= resultDegree;
    sumBoard[r1][c2 + 1] -= resultDegree;
    sumBoard[r2 + 1][c2 + 1] += resultDegree;
  });

  for (let x = 0; x < sumBoard[0].length; x++) {
    for (let y = 1; y < sumBoard.length; y++) {
      sumBoard[y][x] += sumBoard[y - 1][x];
    }
  }

  for (let y = 0; y < sumBoard.length; y++) {
    for (let x = 1; x < sumBoard[0].length; x++) {
      sumBoard[y][x] += sumBoard[y][x - 1];
    }
  }

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      board[y][x] += sumBoard[y][x];
    }
  }

  return board
    .map((coulmn) => {
      return coulmn.filter((v) => v > 0).length;
    })
    .reduce((acc, cur) => (acc += cur));
}
