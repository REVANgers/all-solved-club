// https://programmers.co.kr/learn/courses/30/lessons/86052

const DIRECT = Object.freeze({
  STRAIGHT: 'S',
  LEFT: 'L',
  RIGHT: 'R',
});

const dy = [1, 0, -1, 0];
const dx = [0, 1, 0, -1];

function solution(grid) {
  const answer = [];
  const Y_LENGTH = grid.length;
  const X_LENGTH = grid[0].length;
  const visited = Array.from(Array(Y_LENGTH), () =>
    Array.from(Array(X_LENGTH), () => Array(4).fill(false)),
  );

  console.log(visited);

  for (let y = 0; y < Y_LENGTH; y++) {
    for (let x = 0; x < X_LENGTH; x++) {
      for (let direct = 0; direct < 4; direct++) {
        if (visited[y][x][direct]) {
          continue;
        }

        let nextY = y;
        let nextX = x;
        let nextDirect = direct;

        let count = 0;
        while (!visited[nextY][nextX][nextDirect]) {
          visited[nextY][nextX][nextDirect] = true;
          count++;

          nextY = (nextY + dy[nextDirect] + Y_LENGTH) % Y_LENGTH;
          nextX = (nextX + dx[nextDirect] + X_LENGTH) % X_LENGTH;

          if (grid[nextY][nextX] === DIRECT.LEFT) {
            nextDirect = (nextDirect + 3) % 4;
          } else if (grid[nextY][nextX] === DIRECT.RIGHT) {
            nextDirect = (nextDirect + 1) % 4;
          }
        }
        if (count > 0) {
          answer.push(count);
        }
      }
    }
  }

  return answer.sort((a, b) => a - b);
}
