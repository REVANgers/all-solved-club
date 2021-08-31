// https://www.welcomekakao.com/learn/courses/30/lessons/60058

const isBalanced = string => {
  let left = [];

  for (let current of string) {
    if (current === '(') {
      left.push('(');
    } else {
      if (left.length === 0) {
        return false;
      } else {
        left.pop();
      }
    }
  }

  return left.length === 0 ? true : false;
};

const makeUandV = string => {
  let balance = 0;
  let pivot = 0;

  do {
    balance += string[pivot++] === '(' ? -1 : 1;
  } while (balance !== 0);

  return { u: string.slice(0, pivot), v: string.slice(pivot) };
};

const reverseU = string =>
  string
    .slice(1, string.length - 1)
    .split('')
    .map(c => (c === '(' ? ')' : '('))
    .join('');

const createBalanceString = string => {
  if (string === '') {
    return '';
  }

  if (isBalanced(string)) {
    return string;
  }

  const { u, v } = makeUandV(string);

  const balancedV = createBalanceString(v);

  if (isBalanced(u)) {
    return `${u}${balancedV}`;
  }

  return `(${balancedV})${reverseU(u)}`;
};

function solution(p) {
  return createBalanceString(p);
}
