function solution(board, moves) {
  let deletedCount = 0;
  const map = new Map();
  const stack = [];

  for (let i = 0; i < board.length; i++) {
    map.set(i + 1, []);
  }

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board.length; x++) {
      if (board[y][x] !== 0) {
        map.get(x + 1).push(board[y][x]);
      }
    }
  }

  moves.forEach(index => {
    const doll = map.get(index).shift();

    if (doll) {
      if (stack.length === 0) {
        stack.push(doll);

        return;
      }

      if (stack[stack.length - 1] === doll) {
        stack.pop();
        deletedCount++;
      } else {
        stack.push(doll);
      }
    }
  });

  return deletedCount * 2;
}
