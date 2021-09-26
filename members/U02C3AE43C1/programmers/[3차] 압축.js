function solution(msg) {
  let answer = [];
  const dictionary = new Array(26)
    .fill('A'.charCodeAt(0))
    .map((el, idx) => String.fromCharCode(el + idx));

  while (msg.length > 0) {
    for (let i = dictionary.length - 1; i >= 0; i--) {
      if (msg.indexOf(dictionary[i]) === 0) {
        msg = msg.replace(dictionary[i], '');
        if (!dictionary.includes(dictionary[i] + msg[0])) {
          dictionary.push(dictionary[i] + msg[0]);
        }
        answer.push(i + 1);
        break;
      }
    }
  }

  return answer;
}
