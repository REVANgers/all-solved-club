/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  return bfs(grid);
};

const bfs = grid => {
  const visited = Array.from(Array(grid.length), () =>
    Array(grid[0].length).fill(false),
  );
  const q = [];

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      if (grid[y][x] === 2) {
        visited[y][x] = true;
        q.push({ y, x, time: 0 });
      }
    }
  }

  let lastTime = 0;
  while (q.length > 0) {
    const dy = [1, -1, 0, 0];
    const dx = [0, 0, -1, 1];

    const { y, x, time } = q.shift();
    lastTime = time;

    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (
        nextY < 0 ||
        nextY >= grid.length ||
        nextX < 0 ||
        nextX >= grid[0].length
      ) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      if (grid[nextY][nextX] === 1) {
        grid[nextY][nextX] = 2;
        q.push({ y: nextY, x: nextX, time: time + 1 });
      }
    }
  }

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      if (grid[y][x] === 1) {
        return -1;
      }
    }
  }

  return lastTime;
};
