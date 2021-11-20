/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
  if (grid[0][0] === 1 || grid[grid.length - 1][grid[0].length - 1] === 1) {
    return -1;
  }

  const visited = Array.from(Array(grid.length)).map(() =>
    Array(grid[0].length).fill(false),
  );
  const dy = [1, 1, 1, 0, 0, -1, -1, -1];
  const dx = [-1, 0, 1, -1, 1, -1, 0, 1];
  const q = [{ y: 0, x: 0, visited, length: 1 }];

  while (q.length > 0) {
    const { y, x, visited, length } = q.shift();

    if (y === grid.length - 1 && x === grid[0].length - 1) {
      return length;
    }

    for (let i = 0; i < dy.length; i++) {
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
        continue;
      }

      if (nextY === grid.length - 1 && nextX === grid[0].length - 1) {
        return length + 1;
      }

      visited[nextY][nextX] = true;
      q.push({ y: nextY, x: nextX, visited, length: length + 1 });
    }
  }

  return -1;
};
