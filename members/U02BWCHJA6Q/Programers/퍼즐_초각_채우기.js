// https://programmers.co.kr/learn/courses/30/lessons/84021
// 테스트케이스 6,7 fail

const ON = 1;
const OFF = 0;

function Point(y, x, value) {
  this.y = y;
  this.x = x;
  this.value = value;
}

function Block(points) {
  this.points = points;
  this.onCount = points.filter(point => point.value === ON).length;
  this.offCount = points.filter(point => point.value === OFF).length;
  this.sortPoints = () =>
    this.points.sort((a, b) => {
      if (a.y !== b.y) {
        return a.y - b.y;
      }
      return a.x - b.x;
    });

  this.rotate = () => {
    const board = Array.from(Array(this.yLength), () =>
      Array(this.xLength).fill(OFF),
    );
    const nextBoard = Array.from(Array(this.xLength), () =>
      Array(this.yLength).fill(OFF),
    );

    this.points.forEach(({ y, x }) => (board[y][x - this.minX] = ON));

    for (let y = 0; y < this.yLength; y++) {
      for (let x = 0; x < this.xLength; x++) {
        nextBoard[x][this.yLength - 1 - y] = board[y][x];
      }
    }

    const nextPoints = [];
    let start = false;
    let pivotX, pivotY;

    for (let y = 0; y < this.xLength; y++) {
      for (let x = 0; x < this.yLength; x++) {
        if (nextBoard[y][x] === ON) {
          if (!start) {
            start = true;
            pivotX = x;
            pivotY = y;
          }
          nextPoints.push(new Point(y - pivotY, x - pivotX, ON));
        }
      }
    }

    this.points = nextPoints;
    this.init();
  };

  this.init = () => {
    let minX = 0;
    let maxX = 0;
    let maxY = 0;

    this.points.forEach(({ y, x }) => {
      if (y > maxY) {
        maxY = y;
      }

      if (x > maxX) {
        maxX = x;
      } else if (x < minX) {
        minX = x;
      }
    });

    this.minX = minX;
    this.xLength = maxX - minX + 1;
    this.yLength = maxY + 1;

    this.sortPoints();
  };

  this.init();
}

const makeBlock = (board, pivotY, pivotX, blockStatus, visited) => {
  const dy = [0, 1, 0];
  const dx = [1, 0, -1];
  const y = 0;
  const x = 0;
  const q = [{ y, x }];
  visited[pivotY + y][pivotX + x] = true;
  const points = [new Point(y, x, blockStatus)];

  while (q.length > 0) {
    let { y, x } = q.shift();

    for (let i = 0; i < 3; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (
        nextY + pivotY >= board.length ||
        nextX + pivotX >= board.length ||
        nextX + pivotX < 0
      ) {
        continue;
      }

      if (visited[pivotY + nextY][pivotX + nextX] === true) {
        continue;
      }

      if (board[pivotY + nextY][pivotX + nextX] === blockStatus) {
        visited[pivotY + nextY][pivotX + nextX] = true;
        points.push(new Point(nextY, nextX, blockStatus));
        q.push({ y: nextY, x: nextX });
      }
    }
  }

  return new Block(points);
};

function solution(game_board, table) {
  let answer = 0;
  const LENGTH = game_board.length;
  const emptyList = [];
  const puzzleList = [];

  const boardVisited = Array.from(Array(LENGTH), () =>
    Array(LENGTH).fill(false),
  );
  const tableVisited = Array.from(Array(LENGTH), () =>
    Array(LENGTH).fill(false),
  );

  for (let y = 0; y < LENGTH; y++) {
    for (let x = 0; x < LENGTH; x++) {
      if (game_board[y][x] === ON) {
        continue;
      }
      if (boardVisited[y][x] === true) {
        continue;
      }
      emptyList.push(makeBlock(game_board, y, x, OFF, boardVisited));
    }
  }

  for (let y = 0; y < LENGTH; y++) {
    for (let x = 0; x < LENGTH; x++) {
      if (table[y][x] === OFF) {
        continue;
      }
      if (tableVisited[y][x] === true) {
        continue;
      }
      puzzleList.push(makeBlock(table, y, x, ON, tableVisited));
    }
  }

  emptyList.forEach(emptyBlock => {
    for (let i = 0; i < puzzleList.length; i++) {
      if (emptyBlock.offCount !== puzzleList[i].onCount) {
        continue;
      }

      for (let j = 0; j < 4; j++) {
        if (
          emptyBlock.points.every((point, index) => {
            if (
              point.y === puzzleList[i].points[index].y &&
              point.x === puzzleList[i].points[index].x
            ) {
              return true;
            }
            return false;
          })
        ) {
          answer += emptyBlock.points.length;
          puzzleList.splice(i, 1);
          return;
        } else {
          puzzleList[i].rotate();
        }
      }
    }
  });

  return answer;
}
