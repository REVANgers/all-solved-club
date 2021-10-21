/**
 * @param {number[][]} grid
 * @return {number}
 */

const bfs = (y, x, grid, visited, M, N) => {
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, -1, 1];
  const q = [{ y, x }];

  visited[y][x] = true;
  let count = 0;

  while (q.length > 0) {
    const { y, x } = q.shift();
    count++;

    for (let i = 0; i < dy.length; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (nextY < 0 || nextY >= M || nextX < 0 || nextX >= N) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      if (grid[nextY][nextX] === 0) {
        continue;
      }

      visited[nextY][nextX] = true;
      q.push({ y: nextY, x: nextX });
    }
  }

  return count;
};

var maxAreaOfIsland = function (grid) {
  let max = 0;
  const M = grid.length;
  const N = grid[0].length;

  const visited = Array.from(Array(M), () => Array(N).fill(false));

  for (let y = 0; y < M; y++) {
    for (let x = 0; x < N; x++) {
      if (visited[y][x] || grid[y][x] === 0) {
        continue;
      }

      max = Math.max(max, bfs(y, x, grid, visited, M, N));
    }
  }

  return max;
};
