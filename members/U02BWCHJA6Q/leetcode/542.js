/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
const bfs = (y, x, mat) => {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, -1, 1];
  const visited = Array.from(Array(mat.length), () =>
    Array(mat[0].length).fill(false),
  );
  const q = [];

  for (let y = 0; y < mat.length; y++) {
    for (let x = 0; x < mat[0].length; x++) {
      if (mat[y][x] === 0) {
        visited[y][x] = true;
        q.push({ y, x });
      }
    }
  }

  while (q.length > 0) {
    const { y, x } = q.shift();

    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (
        nextY < 0 ||
        nextY >= mat.length ||
        nextX < 0 ||
        nextX >= mat[0].length
      ) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      visited[nextY][nextX] = true;
      mat[nextY][nextX] += mat[y][x];
      q.push({ y: nextY, x: nextX });
    }
  }
};

var updateMatrix = function (mat) {
  bfs(0, 0, mat);

  return mat;
};
