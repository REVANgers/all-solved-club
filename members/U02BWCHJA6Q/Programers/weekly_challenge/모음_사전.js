// https://programmers.co.kr/learn/courses/30/lessons/84512

let count = 1;

const updateString = (string, index) => {
  let nextString;

  if (string[index] === 'A') {
    count++;
    nextString = string.split('');
    nextString[index] = 'E';
  } else if (string[index] === 'E') {
    count++;
    nextString = string.split('');
    nextString[index] = 'I';
  } else if (string[index] === 'I') {
    count++;
    nextString = string.split('');
    nextString[index] = 'O';
  } else if (string[index] === 'O') {
    count++;
    nextString = string.split('');
    nextString[index] = 'U';
  } else {
    nextString = string.split('');
    console.log(nextString);

    while (nextString[nextString.length - 1] === 'U') {
      nextString.pop();
    }

    return updateString(nextString.join(''), nextString.length - 1);
  }

  return nextString.join('');
};

function solution(word) {
  let string = 'A';

  while (string !== word) {
    if (string.length < 5) {
      string += 'A';
      count++;

      continue;
    }
    if (string.length === 5) {
      string = updateString(string, 4);

      continue;
    }
  }

  return count;
}
