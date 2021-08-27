// https://www.welcomekakao.com/learn/courses/30/lessons/72415

let min = Infinity;

function Position(y, x) {
  this.y = y;
  this.x = x;
}

const getPermutaions = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = [...array.slice(0, index), ...array.slice(index + 1)];
    const restPermutaions = getPermutaions(rest, number - 1);
    const combined = restPermutaions.map(v => [fixed, ...v]);

    result.push(...combined);
  });

  return result;
};

const isPossibleMove = (y, x, length) =>
  y >= 0 && y < length && x >= 0 && x < length;

const ctrlMove = (y, x, dy, dx, board) => {
  let currentY = y;
  let currentX = x;
  let nextY = y + dy;
  let nextX = x + dx;

  while (true) {
    if (!isPossibleMove(nextY, nextX, board.length)) {
      return { nextY: currentY, nextX: currentX };
    }

    if (board[nextY][nextX] !== 0) {
      return { nextY, nextX };
    }

    currentY = nextY;
    currentX = nextX;
    nextY += dy;
    nextX += dx;
  }
};

const bfs = (start, target, board, count) => {
  const visited = Array.from(Array(board.length), () =>
    Array(board.length).fill(false),
  );

  const q = [{ from: start, count }];

  while (q.length > 0) {
    const {
      from: { y, x },
      count,
    } = q.shift();

    if (y === target.y && x === target.x) {
      board[y][x] = 0;

      return { position: target, count: count + 1 };
    }

    const dy = [1, 0, -1, 0];
    const dx = [0, 1, 0, -1];

    for (let i = 0; i < dy.length; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (!isPossibleMove(nextY, nextX, board.length)) {
        continue;
      }

      if (visited[nextY][nextX]) {
        continue;
      }

      visited[nextY][nextX] = true;
      q.push({ from: new Position(nextY, nextX), count: count + 1 });
    }

    for (let i = 0; i < dy.length; i++) {
      const { nextY, nextX } = ctrlMove(y, x, dy[i], dx[i], board);

      if (!visited[nextY][nextX]) {
        visited[nextY][nextX] = true;
        q.push({ from: new Position(nextY, nextX), count: count + 1 });
      }
    }
  }

  return { position: start, count: Infinity };
};

const copyBoard = board => {
  const nextBoard = [];

  board.forEach(row => nextBoard.push([...row]));

  return nextBoard;
};

const dfs = (start, cardMap, cardNumbers, depth, count, board) => {
  if (depth === cardNumbers.length) {
    if (count < min) {
      min = count;
    }

    return;
  }

  const firstCard = cardMap.get(cardNumbers[depth])[0];
  const secondCard = cardMap.get(cardNumbers[depth])[1];

  const normalBoard = copyBoard(board);
  let normal = bfs(start, firstCard, normalBoard, count);

  normal = bfs(normal.position, secondCard, normalBoard, normal.count);
  dfs(
    normal.position,
    cardMap,
    cardNumbers,
    depth + 1,
    normal.count,
    copyBoard(normalBoard),
  );

  const reverseBoard = copyBoard(board);
  let reverse = bfs(start, secondCard, reverseBoard, count);

  reverse = bfs(reverse.position, firstCard, reverseBoard, reverse.count);
  dfs(
    reverse.position,
    cardMap,
    cardNumbers,
    depth + 1,
    reverse.count,
    copyBoard(reverseBoard),
  );
};

function solution(board, r, c) {
  const answer = 0;
  const cardMap = new Map();
  const LENGTH = 4;

  for (let y = 0; y < LENGTH; y++) {
    for (let x = 0; x < LENGTH; x++) {
      const cardNumber = board[y][x];

      if (cardNumber === 0) {
        continue;
      }

      if (!cardMap.has(cardNumber)) {
        cardMap.set(cardNumber, [new Position(y, x)]);
      } else {
        cardMap.get(cardNumber).push(new Position(y, x));
      }
    }
  }

  const cardNumbers = [...cardMap].map(([cardNumber, _]) => cardNumber);
  const combinations = getPermutaions(cardNumbers, cardNumbers.length);

  const start = new Position(r, c);
  combinations.forEach(currentCardNumbers => {
    dfs(start, cardMap, currentCardNumbers, 0, 0, board);
  });

  return min;
}
