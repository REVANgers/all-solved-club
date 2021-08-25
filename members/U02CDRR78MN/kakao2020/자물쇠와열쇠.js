// 옛날풀이보다 풀이가 깔끔해졌다💪

function solution(key, lock) {
  const keySize = key.length;
  const lockSize = lock.length;

  const rotate = (board) =>
    board.map((row, r) =>
      row.map((block, c) => board[c][board.length - 1 - r])
    );

  const emptyCount = lock
    .map((row) => row.filter((block) => !block).length)
    .reduce((acc, c) => acc + c);
  if (emptyCount > keySize ** 2) {
    return false;
  }

  // 평행 이동
  for (let dx = -keySize + 1; dx < lockSize; dx++) {
    for (let dy = -keySize + 1; dy < lockSize; dy++) {
      let rotated;

      // 열쇠 회전
      for (let i = 0; i < 4; i++) {
        rotated = rotate(rotated || key);
        let count = emptyCount;
        let collision = false;

        // 확인
        for (let x = 0; x < keySize; x++) {
          for (let y = 0; y < keySize; y++) {
            if (collision) {
              y = keySize;
              x = keySize;
              break;
            }

            const keyBlock = rotated[y][x];

            const xx = x + dx;
            const yy = y + dy;

            if (xx < 0 || xx >= lockSize || yy < 0 || yy >= lockSize) {
              continue;
            }

            if (lock[yy][xx] && keyBlock) {
              collision = true;
            }

            if (!lock[yy][xx] && keyBlock) {
              count--;
            }

            if (count === 0) {
              return true;
            }
          }
        }
      }
    }
  }

  return false;
}
