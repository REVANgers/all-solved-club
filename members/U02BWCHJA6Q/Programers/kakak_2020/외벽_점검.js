// https://programmers.co.kr/learn/courses/30/lessons/60062

const rotate = (weak, n) => [...weak.slice(1), weak[0] + n];

const getPermutation = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = [...array.slice(0, index), ...array.slice(index + 1)];
    const restCombination = getPermutation(rest, number - 1);
    const combine = restCombination.map(v => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
};

function solution(n, weak, dist) {
  let answer = -1;

  for (let i = 1; i <= dist.length; i++) {
    const permutations = getPermutation(dist, i);

    if (
      permutations.some(friends => {
        for (let i = 0; i < weak.length; i++) {
          weak = rotate(weak, n);
          const distances = [...weak];

          if (
            friends.some(friend => {
              const current = distances.shift() + friend;

              while (true) {
                if (current >= distances[0]) {
                  distances.shift();
                } else {
                  break;
                }
              }

              if (distances.length === 0) {
                return true;
              }
            })
          ) {
            answer = friends.length;

            return true;
          }
        }
        return false;
      })
    ) {
      return answer;
    }
  }

  return answer;
}
