function solution(n, info) {
  const MAX_SCORE = 10;
  let answer = [-1];
  let maxScoreDifference = 0;

  const getScoreDifference = (appeachScoreInfo, ryanScoreInfo) => {
    let appeachScore = 0;
    let ryanScore = 0;

    for (let i = 0; i < 10; i++) {
      if (appeachScoreInfo[i] === 0 && ryanScoreInfo[i] === 0) {
        continue;
      }

      if (appeachScoreInfo[i] >= ryanScoreInfo[i]) {
        appeachScore += MAX_SCORE - i;

        continue;
      }

      ryanScore += MAX_SCORE - i;
    }

    return ryanScore - appeachScore;
  };

  const dfs = (index, count, scores) => {
    if (index === -1 && count === n) {
      const scoreDifference = getScoreDifference(info, scores);

      if (maxScoreDifference < scoreDifference) {
        maxScoreDifference = scoreDifference;
        answer = scores;
      }

      return;
    }

    if (index === -1) {
      return;
    }

    if (count === n) {
      const scoreDifference = getScoreDifference(info, scores);

      if (maxScoreDifference < scoreDifference) {
        maxScoreDifference = scoreDifference;
        answer = scores;
      }

      return;
    }

    for (let i = n - count; i >= 0; i--) {
      const nextScores = [...scores];

      nextScores[index] = i;

      dfs(index - 1, i + count, nextScores);
    }
  };

  const scores = Array(MAX_SCORE + 1).fill(0);
  dfs(MAX_SCORE, 0, scores);

  return answer;
}
