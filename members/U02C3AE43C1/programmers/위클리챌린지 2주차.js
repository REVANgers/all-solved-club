function getGrade(avg) {
  if (avg >= 90) {
    return 'A';
  } else if (avg >= 80) {
    return 'B';
  } else if (avg >= 70) {
    return 'C';
  } else if (avg >= 50) {
    return 'D';
  } else {
    return 'F';
  }
}

function solution(scores) {
  let answer = '';

  scores = scores.map((el, idx) => scores.map((el) => el[idx]));

  scores.forEach((score, idx) => {
    const max = Math.max(...score);
    const min = Math.min(...score);

    if (score[idx] === max && score.filter((el) => el === max).length === 1) {
      score.splice(idx, 1);
    } else if (score[idx] === min && score.filter((el) => el === min).length === 1) {
      score.splice(idx, 1);
    }

    const avg = score.reduce((acc, cur) => acc + cur, 0) / score.length;

    answer += getGrade(avg);
  });

  return answer;
}
