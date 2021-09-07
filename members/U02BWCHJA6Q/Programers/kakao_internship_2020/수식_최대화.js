// https://programmers.co.kr/learn/courses/30/lessons/67257

const getPermutation = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = [...array.slice(0, index), ...array.slice(index + 1)];
    const restPermutation = getPermutation(rest, number - 1);
    const combined = restPermutation.map(v => [fixed, ...v]);

    result.push(...combined);
  });

  return result;
};

const calculate = (left, right, operator) => {
  if (operator === '+') {
    return left + right;
  }
  if (operator === '-') {
    return left - right;
  }
  if (operator === '*') {
    return left * right;
  }
};

const getResult = (numbers, operators, priority) => {
  for (const currentPriority of priority) {
    for (let i = 0; i < operators.length; i++) {
      if (operators[i] === currentPriority) {
        const result = calculate(
          Number(numbers[i]),
          Number(numbers[i + 1]),
          operators[i],
        );
        numbers.splice(i, 2, result);
        operators.splice(i, 1);
        i--;
      }
    }
  }

  return Math.abs(numbers[0]);
};

function solution(expression) {
  let max = 0;
  const numbers = expression.match(/\d+/g);
  const operators = expression.match(/[-*+]+/g);
  const operatorSet = new Set(operators);
  const operatorPriorities = getPermutation([...operatorSet], operatorSet.size);

  operatorPriorities.forEach(priority => {
    max = Math.max(max, getResult([...numbers], [...operators], priority));
  });

  return max;
}
