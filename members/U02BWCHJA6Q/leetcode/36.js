/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  const SIZE = 9;

  for (let y = 0; y < SIZE; y++) {
    const set = new Set();
    for (let x = 0; x < SIZE; x++) {
      if (!isNaN(board[y][x])) {
        if (set.has(board[y][x])) {
          return false;
        }
        set.add(board[y][x]);
      }
    }
  }

  for (let x = 0; x < SIZE; x++) {
    const set = new Set();
    for (let y = 0; y < SIZE; y++) {
      if (!isNaN(board[y][x])) {
        if (set.has(board[y][x])) {
          return false;
        }
        set.add(board[y][x]);
      }
    }
  }

  for (let dy = 0; dy < 3; dy++) {
    for (let dx = 0; dx < 3; dx++) {
      const set = new Set();
      for (let y = 0 + dy * 3; y < 3 + dy * 3; y++) {
        for (let x = 0 + dx * 3; x < 3 + dx * 3; x++) {
          if (!isNaN(board[y][x])) {
            if (set.has(board[y][x])) {
              return false;
            }
            set.add(board[y][x]);
          }
        }
      }
    }
  }

  return true;
};
