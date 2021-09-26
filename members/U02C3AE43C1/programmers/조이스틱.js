function solution(name) {
  let answer = 0;
  let str = [...'A'.repeat(name.length)];
  let curIdx = 0;
  name = [...name];

  while (true) {
    const forward = name[curIdx].charCodeAt(0) - 'A'.charCodeAt(0);
    const backward = 'Z'.charCodeAt(0) - name[curIdx].charCodeAt(0) + 1;

    answer += forward > backward ? backward : forward;

    str[curIdx] = name[curIdx];

    curIdx = findIndex();

    if (name.join('') === str.join('')) break;
  }

  return answer;

  function findIndex() {
    let minDiff = 20;
    let idx = 0;

    for (let i = 0; i < name.length; i++) {
      if (name[i] === 'A' || name[i] === str[i]) continue;
      const forwordDiff = Math.abs(curIdx - i);
      const backwordDiff = Math.abs(curIdx + name.length - i);
      const diff = forwordDiff > backwordDiff ? backwordDiff : forwordDiff;

      if (diff < minDiff) {
        minDiff = diff;
        idx = i;
      }
    }

    answer += minDiff < 20 ? minDiff : 0;

    return idx;
  }
}
