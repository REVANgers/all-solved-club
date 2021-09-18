// https://programmers.co.kr/learn/courses/30/lessons/67258

function solution(gems) {
  const gemsSize = new Set(gems).size;
  const gemsMap = new Map();
  const MAX = 100000;
  let answer = [0, MAX];

  gems.forEach((gem, index) => {
    gemsMap.delete(gem);
    gemsMap.set(gem, index);

    if (gemsMap.size == gemsSize) {
      const start = gemsMap.values().next().value;
      const end = index;

      if (end - start < answer[1] - answer[0]) {
        answer = [start + 1, end + 1];
      }
      gemsMap.delete(gems[start]);
    }
  });

  return answer;
}
