// https://programmers.co.kr/learn/courses/30/lessons/85002

function solution(weights, head2head) {
  return head2head
    .map((match, index) => {
      let total = 0;
      let win = 0;
      let winByHeavy = 0;
      const weight = weights[index];

      for (let i = 0; i < match.length; i++) {
        if (match[i] === 'N') {
          continue;
        }

        total++;
        if (match[i] === 'W') {
          win++;

          if (weights[i] > weight) {
            winByHeavy++;
          }
        }
      }

      const winRate = win === 0 ? 0 : win / total;

      return {
        winRate,
        winByHeavy,
        weight,
        index: index + 1,
        weight: weights[index],
      };
    })
    .sort((a, b) => {
      if (a.winRate !== b.winRate) {
        return b.winRate - a.winRate;
      }
      if (a.winByHeavy !== b.winByHeavy) {
        return b.winByHeavy - a.winByHeavy;
      }
      if (a.weight !== b.weight) {
        return b.weight - a.weight;
      }
      return a.index - b.index;
    })
    .map(({ index }) => index);
}
