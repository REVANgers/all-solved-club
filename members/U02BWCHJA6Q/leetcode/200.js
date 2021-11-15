/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const bfs = (y, x, visited) => {
    const dy = [1, -1, 0, 0];
    const dx = [0, 0, -1, 1];
    const q = [{ y, x }];

    while (q.length > 0) {
      const { y, x } = q.shift();

      for (let i = 0; i < 4; i++) {
        const nextY = y + dy[i];
        const nextX = x + dx[i];

        if (nextY < 0 || nextY >= grid.length || x < 0 || x >= grid[0].length) {
          continue;
        }

        if (visited[nextY][nextX]) {
          continue;
        }

        if (grid[nextY][nextX] === '0') {
          continue;
        }

        visited[nextY][nextX] = true;
        q.push({ y: nextY, x: nextX });
      }
    }
  };

  const visited = Array.from(Array(grid.length), () =>
    Array(grid[0].length).fill(false),
  );
  let count = 0;

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      if (!visited[y][x] && grid[y][x] === '1') {
        visited[y][x] = true;
        bfs(y, x, visited);
        count++;
      }
    }
  }

  return count;
};
