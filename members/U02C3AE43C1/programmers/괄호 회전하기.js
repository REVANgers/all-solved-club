function isCorrect(str) {
  const stack = [];

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    const stackTop = stack.length - 1;

    if (stackTop === -1) {
    } else if (char === '}') {
      if (stack[stackTop] === '{') {
        stack.pop();
        continue;
      }
    } else if (char === ']') {
      if (stack[stackTop] === '[') {
        stack.pop();
        continue;
      }
    } else if (char === ')') {
      if (stack[stackTop] === '(') {
        stack.pop();
        continue;
      }
    }

    stack.push(char);
  }

  return stack.length === 0;
}

function rotate(str, n) {
  const temp = [...str];

  for (let i = 0; i < n; i++) {
    temp.push(temp.shift());
  }

  return temp.join('');
}

function solution(s) {
  let answer = 0;

  if (s.length % 2 === 1) {
    return 0;
  }

  for (let i = 0; i < s.length; i++) {
    if (isCorrect(rotate(s, i))) {
      answer += 1;
    }
  }

  return answer;
}
