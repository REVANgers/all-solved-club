function solution(n, m, x, y, queries) {
  const LEFT = 0;
  const RIGHT = 1;
  const UP = 2;
  const DOWN = 3;

  let startX = y;
  let endX = y;
  let startY = x;
  let endY = x;

  for (let i = queries.length - 1; i >= 0; i--) {
    const [direct, distance] = queries[i];

    if (direct === LEFT) {
      if (startX !== 0) {
        startX += distance;
      }

      endX += distance;

      if (endX > m - 1) {
        endX = m - 1;
      }
    } else if (direct === RIGHT) {
      startX -= distance;

      if (startX < 0) {
        startX = 0;
      }

      if (endX !== m - 1) {
        endX -= distance;
      }
    } else if (direct === UP) {
      if (startY !== 0) {
        startY += distance;
      }

      endY += distance;

      if (endY > n - 1) {
        endY = n - 1;
      }
    } else if (direct === DOWN) {
      startY -= distance;
      if (startY < 0) {
        startY = 0;
      }
      if (endY !== n - 1) {
        endY -= distance;
      }
    }

    if (
      startY > n - 1 ||
      endY < 0 ||
      startX > m - 1 ||
      endX < 0 ||
      startY > endY ||
      startX > endX
    ) {
      return 0;
    }
  }

  return BigInt(endY - startY + 1) * BigInt(endX - startX + 1);
}
