const getCombinations = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map((v) => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = array.slice(index + 1);
    const restCombinations = getCombinations(rest, number - 1);
    const combined = restCombinations.map((v) => [fixed, ...v]);

    result.push(...combined);
  });

  return result;
};

function solution(line) {
  const answer = [];

  const getPoint = ([A, B, E], [C, D, F]) => {
    return {
      x: (B * F - E * D) / (A * D - B * C),
      y: (E * C - A * F) / (A * D - B * C),
    };
  };

  const isNumber = (number) => number % 1 === 0;

  const combinations = getCombinations(line, 2);
  const points = combinations
    .filter(([[A, B, E], [C, D, F]]) => A * D - B * C !== 0)
    .map(([a, b]) => getPoint(a, b))
    .filter(({ y, x }) => isNumber(y) && isNumber(x));

  let minX = Infinity;
  let maxX = -Infinity;
  let minY = Infinity;
  let maxY = -Infinity;

  points.forEach(({ y, x }) => {
    if (x < minX) {
      minX = x;
    }
    if (x > maxX) {
      maxX = x;
    }
    if (y < minY) {
      minY = y;
    }
    if (y > maxY) {
      maxY = y;
    }
  });

  const board = Array.from(Array(maxY - minY + 1), () =>
    Array(maxX - minX + 1).fill('.')
  );

  points.forEach(({ y, x }) => (board[maxY - y][x - minX] = '*'));

  return board.map((v) => v.join(''));
}
