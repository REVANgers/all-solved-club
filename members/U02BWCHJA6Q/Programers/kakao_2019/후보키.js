// https://programmers.co.kr/learn/courses/30/lessons/42890

const getCombination = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = array.slice(index + 1);
    const restCombination = getCombination(rest, number - 1);
    const combined = restCombination.map(v => [fixed, ...v]);

    result.push(...combined);
  });

  return result;
};

function solution(relation) {
  const COLUMN_LENGTH = relation[0].length;
  const candidateIndexSet = new Set();
  let answer = 0;
  let columnIndex = [];

  for (let i = 0; i < COLUMN_LENGTH; i++) {
    columnIndex.push(i);
  }

  for (let i = 1; i <= COLUMN_LENGTH; i++) {
    const combinations = getCombination(columnIndex, i);

    combinations.forEach(([...indexes]) => {
      if (
        [...candidateIndexSet].some(candidateIndex =>
          candidateIndex.every(index => indexes.includes(index)),
        )
      ) {
        return;
      }

      const set = new Set();

      relation.forEach(tuple => {
        let key = '';

        indexes.forEach(index => (key = `${key}-${tuple[index]}`));
        set.add(key);
      });

      if (set.size === relation.length) {
        answer++;
        candidateIndexSet.add(indexes);
      }
    });
  }

  return answer;
}
