// https://programmers.co.kr/learn/courses/30/lessons/67259

const nextPosition = [
  [0, -1],
  [0, 1],
  [-1, 0],
  [1, 0],
];

const bfs = (board, y, x, min) => {
  const size = board.length;
  let direct = -1;
  let cost = 0;
  const visited = Array.from(Array(size), () => Array(size).fill(0));

  if (board[y][x] === 1) {
    y = 0;
    x = 0;
    cost = 0;
  } else {
    y === 1 ? (direct = 3) : (direct = 1);
    cost = 100;
    visited[y][x] = cost;
  }

  const q = [{ y, x, direct, cost }];

  while (q.length > 0) {
    const { y, x, direct, cost } = q[0];
    q.shift();

    if (min < cost) {
      continue;
    }

    if (y === size - 1 && x === size - 1) {
      if (min > cost) {
        min = cost;
        continue;
      }
    }

    for (let i = 0; i < 4; i++) {
      const nextY = y + nextPosition[i][0];
      const nextX = x + nextPosition[i][1];
      let nextCost = cost + 100;

      if (nextY < 0 || nextY >= size || nextX < 0 || nextX >= size) {
        continue;
      }

      if (board[nextY][nextX] === 1) {
        continue;
      }

      if (direct !== i) {
        nextCost += 500;
      }

      if (visited[nextY][nextX] === 0 || visited[nextY][nextX] >= nextCost) {
        visited[nextY][nextX] = nextCost;
        q.push({ y: nextY, x: nextX, direct: i, cost: nextCost });
      }
    }
  }

  return min;
};

function solution(board) {
  let min = bfs(board, 1, 0, Infinity);
  console.log(min);
  return bfs(board, 0, 1, min);
}
