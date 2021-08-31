// https://www.welcomekakao.com/learn/courses/30/lessons/60057

const zipString = (string, number) => {
  let zipped = '';
  let pivot = number;
  let current = string.slice(0, number);
  let count = 1;

  while (pivot < string.length) {
    const next = string.slice(pivot, pivot + number);

    if (current === next) {
      count++;
    } else {
      zipped += `${count === 1 ? '' : count}${current}`;
      current = next;
      count = 1;
    }
    pivot += number;

    if (pivot >= string.length) {
      zipped += `${count === 1 ? '' : count}${current}`;
    }
  }

  return zipped;
};

function solution(s) {
  const MAX = Math.floor(s.length / 2);
  let min = Infinity;

  if (s.length === 1) {
    return 1;
  }

  for (let i = 1; i <= MAX; i++) {
    const zipped = zipString(s, i);

    if (min > zipped.length) {
      min = zipped.length;
    }
  }

  return min;
}
