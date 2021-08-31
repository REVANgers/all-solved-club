// https://programmers.co.kr/learn/courses/30/lessons/42889

function solution(N, stages) {
  let answer = [];
  const map = new Map();

  stages.sort((a, b) => a - b);
  stages.forEach(level => {
    if (!map.has(level)) {
      map.set(level, 1);
    } else {
      map.set(level, map.get(level) + 1);
    }
  });

  let total = stages.length;
  const failureList = [];

  for (let i = 1; i <= N; i++) {
    const count = map.get(i);

    if (!count) {
      failureList.push({ index: i, failure: 0 });

      continue;
    }

    const failure = count / total;
    failureList.push({ index: i, failure });

    total -= count;
  }

  return failureList
    .sort((a, b) => {
      if (a.failure !== b.failure) {
        return b.failure - a.failure;
      }

      return a.index - b.index;
    })
    .map(({ index }) => index);
}
