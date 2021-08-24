function solution(msg) {
  var answer = [];

  const indexes = new Map();

  Array(26)
    .fill(0)
    .map((_, i) => String.fromCharCode(i + 65))
    .forEach((alpha, i) => {
      indexes.set(alpha, indexes.size + 1);
    });

  let current = 0;
  let str = "";

  while (current < msg.length) {
    str += msg[current];

    if (!indexes.has(str)) {
      answer.push(indexes.get(str.slice(0, -1)));

      indexes.set(str, indexes.size + 1);
      str = "";
      continue;
    }

    current++;
  }

  answer.push(indexes.get(str));

  return answer;
}
