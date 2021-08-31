// https://programmers.co.kr/learn/courses/30/lessons/60063

function Robot(left, right) {
  this.left = left;
  this.right = right;
}

function Position(y, x) {
  this.y = y;
  this.x = x;
}

const isInBoard = (y, x, boardSize) =>
  y >= 0 && y < boardSize && x >= 0 && x < boardSize;

const isVisited = (left, right, visited) =>
  visited.some(([visitedLeft, visitedRight]) => {
    const sameLeft = visitedLeft.y === left.y && visitedLeft.x === left.x;
    const sameRight = visitedRight.y === right.y && visitedRight.x === right.x;
    return sameLeft && sameRight ? true : false;
  });

const bfs = (robot, board, visited) => {
  let count = 0;
  const BOARD_SIZE = board.length;
  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];
  const q = [{ robot, count }];

  while (q.length > 0) {
    const { robot, count } = q.shift();

    if (robot.left.y === BOARD_SIZE - 1 && robot.left.x === BOARD_SIZE - 1) {
      return count;
    }
    if (
      robot.right.y === board.length - 1 &&
      robot.right.x === board.length - 1
    ) {
      return count;
    }

    for (let i = 0; i < dy.length; i++) {
      const nextLeft = new Position(robot.left.y + dy[i], robot.left.x + dx[i]);
      const nextRight = new Position(
        robot.right.y + dy[i],
        robot.right.x + dx[i],
      );
      if (
        !(
          isInBoard(nextLeft.y, nextLeft.x, BOARD_SIZE) &&
          isInBoard(nextRight.y, nextRight.x, BOARD_SIZE)
        )
      ) {
        continue;
      }

      if (
        board[nextLeft.y][nextLeft.x] === 1 ||
        board[nextRight.y][nextRight.x] === 1
      ) {
        continue;
      }

      if (isVisited(nextLeft, nextRight, visited)) {
        continue;
      }

      const nextRobot = new Robot(nextLeft, nextRight);

      visited.push([nextLeft, nextRight], [nextRight, nextLeft]);
      q.push({ robot: nextRobot, count: count + 1 });
    }

    if (robot.left.y === robot.right.y) {
      for (let i of [-1, 1]) {
        const nextLeft = new Position(robot.left.y + i, robot.left.x);
        const nextRight = new Position(robot.right.y + i, robot.right.x);

        if (
          !(
            isInBoard(nextLeft.y, nextLeft.x, BOARD_SIZE) &&
            isInBoard(nextRight.y, nextRight.x, BOARD_SIZE)
          )
        ) {
          continue;
        }

        if (
          board[nextLeft.y][nextLeft.x] === 0 &&
          board[nextRight.y][nextRight.x] === 0
        ) {
          if (!isVisited(robot.left, nextLeft, visited)) {
            visited.push([robot.left, nextLeft], [nextLeft, robot.left]);
            q.push({
              robot: new Robot(robot.left, nextLeft),
              count: count + 1,
            });
          }
          if (!isVisited(robot.right, nextRight, visited)) {
            visited.push([robot.right, nextRight], [nextRight, robot.right]);
            q.push({
              robot: new Robot(robot.right, nextRight),
              count: count + 1,
            });
          }
        }
      }
    } else {
      for (let i of [-1, 1]) {
        const nextLeft = new Position(robot.left.y, robot.left.x + i);
        const nextRight = new Position(robot.right.y, robot.right.x + i);

        if (
          !(
            isInBoard(nextLeft.y, nextLeft.x, BOARD_SIZE) &&
            isInBoard(nextRight.y, nextRight.x, BOARD_SIZE)
          )
        ) {
          continue;
        }

        if (
          board[nextLeft.y][nextLeft.x] === 0 &&
          board[nextRight.y][nextRight.x] === 0
        ) {
          if (!isVisited(robot.left, nextLeft, visited)) {
            visited.push([robot.left, nextLeft], [nextLeft, robot.left]);
            q.push({
              robot: new Robot(robot.left, nextLeft),
              count: count + 1,
            });
          }
          if (!isVisited(robot.right, nextRight, visited)) {
            visited.push([robot.right, nextRight], [nextRight, robot.right]);
            q.push({
              robot: new Robot(robot.right, nextRight),
              count: count + 1,
            });
          }
        }
      }
    }
  }
};

function solution(board) {
  const left = new Position(0, 0);
  const right = new Position(0, 1);
  const robot = new Robot(left, right);
  const visited = [
    [left, right],
    [right, left],
  ];

  return bfs(robot, board, visited);
}
