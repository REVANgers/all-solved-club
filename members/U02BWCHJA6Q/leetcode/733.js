/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  const color = image[sr][sc];
  image[sr][sc] = newColor;

  const q = [{ y: sr, x: sc }];
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, -1, 1];
  const visited = Array.from(Array(image.length), () =>
    Array(image[0].length).fill(false),
  );
  visited[sr][sc] = true;

  while (q.length > 0) {
    const { y, x } = q.shift();

    for (let i = 0; i < dy.length; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (
        nextY < 0 ||
        nextY >= image.length ||
        nextX < 0 ||
        nextX >= image[0].length
      ) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      if (image[nextY][nextX] !== color) {
        continue;
      }

      visited[nextY][nextX] = true;
      image[nextY][nextX] = newColor;
      q.push({ y: nextY, x: nextX });
    }
  }

  return image;
};
