function trans(str) {
  if (str === '') return '';

  let u = '',
    v = '';

  for (let i = 0, lCnt = 0, rCnt = 0; i < str.length; i++) {
    if (str[i] === '(') {
      lCnt += 1;
    } else {
      rCnt += 1;
    }

    if (lCnt === rCnt) {
      u = str.slice(0, i + 1);
      v = str.slice(i + 1);
      break;
    }
  }

  if (u[0] === '(') {
    return u + trans(v);
  }

  u = [...u.slice(1, u.length - 1)].map((char) => (char === '(' ? ')' : '(')).join('');

  return '(' + trans(v) + ')' + u;
}

function solution(p) {
  return trans(p);
}

// function trans(str) {
//     if(str === '') return '';

//     let u = '', v = '';

//     for(let i = 0, lCnt = 0, rCnt = 0;i < str.length;i++) {
//         if(str[i] === '(') {
//             lCnt += 1;
//         } else {
//             rCnt += 1;
//         }

//         if(lCnt === rCnt) {
//             u = str.slice(0, i + 1);
//             v = str.slice(i + 1);
//             break;
//         }
//     }

//     if(isCorrect(u)) return u + trans(v);

//     u = [...u.slice(1, u.length - 1)]
//         .map(char => char === '(' ? ')' : '(')
//         .join('');

//     return '(' + trans(v) + ')' + u;
// }

// function isCorrect(str) {
//     const stack = [];

//     [...str].forEach(char => {
//         if(stack.length === 0) {
//             stack.push(char);
//         } else if(char === '(') {
//             stack.push(char);
//         } else {
//             if(stack[stack.length - 1] === '(') {
//                 stack.pop();
//             } else {
//                 stack.push(char);
//             }
//         }
//     });

//     return stack.length === 0;
// }

// function solution(p) {
//     return trans(p);
// }
