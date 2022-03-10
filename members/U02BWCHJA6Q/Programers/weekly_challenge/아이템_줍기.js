function solution(rectangle, characterX, characterY, itemX, itemY) {
  const MAX = 50;
  const MULTIPLY = 2;
  const board = Array.from(Array(MAX * MULTIPLY + 1), () =>
    Array(MAX * MULTIPLY + 1).fill(0)
  );
  const visited = Array.from(Array(MAX * MULTIPLY + 1), () =>
    Array(MAX * MULTIPLY + 1).fill(false)
  );
  const ON = 1;
  const OFF = 0;

  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let y = y1 * MULTIPLY; y <= y2 * MULTIPLY; y++) {
      for (let x = x1 * MULTIPLY; x <= x2 * MULTIPLY; x++) {
        board[y][x] = ON;
      }
    }
  });

  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let y = y1 * MULTIPLY + 1; y < y2 * MULTIPLY; y++) {
      for (let x = x1 * MULTIPLY + 1; x < x2 * MULTIPLY; x++) {
        board[y][x] = OFF;
      }
    }
  });

  const q = [{ y: characterY * MULTIPLY, x: characterX * MULTIPLY, count: 0 }];
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, -1, 1];
  visited[characterY * MULTIPLY][characterX * MULTIPLY] = true;

  while (q.length > 0) {
    const { y, x, count } = q.shift();

    if (y === itemY * MULTIPLY && x === itemX * MULTIPLY) {
      return count / 2;
    }

    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (
        nextX < 0 ||
        nextX > MAX * MULTIPLY ||
        nextY < 0 ||
        nextY > MAX * MULTIPLY
      ) {
        continue;
      }

      if (board[nextY][nextX] !== ON) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      visited[nextY][nextX] = true;
      q.push({ y: nextY, x: nextX, count: count + 1 });
    }
  }

  return -1;
}
