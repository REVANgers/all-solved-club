function solution(relation) {
  var answer = 0;

  const relationSize = relation[0].length;
  const tuples = Array(relationSize)
    .fill(0)
    .map((_, i) => i);
  const minimals = [];

  const combination = (arr, r) => {
    if (r === 1) {
      return arr.map((el) => [el]);
    }

    const combs = [];

    arr.forEach((el, i) => {
      const smallerCombs = combination(arr.slice(i + 1), r - 1);

      smallerCombs.forEach((smallerComb) => {
        combs.push([el, ...smallerComb]);
      });
    });

    return combs;
  };

  const isUnique = (tuples) => {
    const set = new Set();

    for (const rel of relation) {
      const key = tuples.map((tuple) => rel[tuple]).join(",");

      if (set.has(key)) return false;

      set.add(key);
    }

    return true;
  };

  const isMinimal = (tuples) =>
    minimals.some((m) =>
      m.every(
        (minTuple) => tuples.findIndex((tuple) => tuple === minTuple) !== -1
      )
    )
      ? false
      : true;

  for (let r = 1; r <= relationSize; r++) {
    const combs = combination(tuples, r);

    combs.forEach((comb) => {
      if (isUnique(comb) && isMinimal(comb)) {
        minimals.push(comb);

        answer += 1;
      }
    });
  }

  return answer;
}
