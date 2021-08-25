function solution(n, build_frame) {
  const size = n + 1;
  const board = ["ki", "bo"].map((type) =>
    Array(size)
      .fill(0)
      .map((_) => Array(size).fill(0))
  );

  const canBuild = (x, y, type) => {
    const ki = board[0];
    const bo = board[1];

    // 보
    if (type === 1) {
      // 보 사이
      if (bo[y][x - 1] && bo[y][x + 1]) {
        return true;
      }

      // 기둥 위
      if (ki[y - 1][x] || ki[y - 1][x + 1]) {
        return true;
      }
    }

    // 기둥
    if (type === 0) {
      // 바닥 위
      if (y === 0) {
        return true;
      }
      // 보 위
      if (bo[y][x - 1] || bo[y][x]) {
        return true;
      }
      // 기둥 위
      if (y > 0 && ki[y - 1][x]) {
        return true;
      }
    }

    return false;
  };

  const canDelete = (x, y, type) => {
    for (let dx = -2; dx < 3; dx++) {
      for (let dy = -1; dy < 2; dy++) {
        for (let type = 0; type < 2; type++) {
          const xx = x + dx;
          const yy = y + dy;

          if (xx < 0 || yy < 0 || xx >= size || yy >= size) {
            continue;
          }

          if (board[type][yy][xx] && !canBuild(xx, yy, type)) {
            return false;
          }
        }
      }
    }

    return true;
  };

  // 입력
  build_frame.forEach(([x, y, type, action]) => {
    // 설치
    if (action === 1 && canBuild(x, y, type)) {
      board[type][y][x] = 1;
    }

    // 삭제
    if (action === 0) {
      board[type][y][x] = 0;

      if (!canDelete(x, y, type)) {
        board[type][y][x] = 1;
      }
    }
  });

  // <[x,y,타입]>[] x좌표 오름차순, y좌표 오름차순
  const ans = [];

  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      board.forEach((structures, type) => {
        structures[y][x] && ans.push([x, y, type]);
      });
    }
  }

  return ans;
}
