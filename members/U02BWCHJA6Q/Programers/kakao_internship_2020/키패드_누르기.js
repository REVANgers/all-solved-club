// https://programmers.co.kr/learn/courses/30/lessons/67256

function Point(y, x) {
  this.y = y;
  this.x = x;
}

function solution(numbers, hand) {
  let answer = '';
  const keypadMap = {};
  let number = 1;

  for (let y = 0; y < 3; y++) {
    for (let x = 0; x < 3; x++) {
      keypadMap[number] = new Point(y, x);
      number++;
    }
  }

  keypadMap['*'] = new Point(3, 0);
  keypadMap[0] = new Point(3, 1);
  keypadMap['#'] = new Point(3, 2);

  let left = keypadMap['*'];
  let right = keypadMap['#'];

  numbers.forEach(number => {
    if (number === 1 || number === 4 || number === 7) {
      left = keypadMap[number];
      answer += 'L';

      return;
    }

    if (number === 3 || number === 6 || number === 9) {
      right = keypadMap[number];
      answer += 'R';

      return;
    }

    const { y, x } = keypadMap[number];
    const leftDistance = Math.abs(left.y - y) + Math.abs(left.x - x);
    const rightDistance = Math.abs(right.y - y) + Math.abs(right.x - x);

    if (leftDistance === rightDistance) {
      if (hand === 'left') {
        left = keypadMap[number];
        answer += 'L';
      } else {
        right = keypadMap[number];
        answer += 'R';
      }

      return;
    }

    if (leftDistance < rightDistance) {
      left = keypadMap[number];
      answer += 'L';
    } else {
      right = keypadMap[number];
      answer += 'R';
    }
  });

  return answer;
}
