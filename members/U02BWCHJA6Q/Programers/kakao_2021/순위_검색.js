// https://programmers.co.kr/learn/courses/30/lessons/72412

function solution(info, query) {
  const answer = [];
  const infoMap = {};

  const setInfoMap = (info, score, start) => {
    const key = info.join('');

    if (!infoMap[key]) {
      infoMap[key] = [];
    }
    infoMap[key].push(score);

    for (let i = start; i < info.length; i++) {
      const nextInfo = [...info];

      nextInfo[i] = '-';
      setInfoMap(nextInfo, score, i + 1);
    }
  };

  info.forEach(string => {
    const splited = string.split(' ');
    const score = Number(splited.pop());

    setInfoMap(splited, score, 0);
  });

  for (let key in infoMap) {
    infoMap[key].sort((a, b) => a - b);
  }

  query.forEach(string => {
    const splited = string.split(' ');
    const score = Number(splited.pop());
    const key = splited.filter(s => s !== 'and').join('');
    const scoreList = infoMap[key];

    if (!scoreList) {
      answer.push(0);
    } else {
      let left = 0;
      let right = scoreList.length - 1;

      while (left <= right) {
        let mid = Math.floor((right + left) / 2);

        if (scoreList[mid] < score) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
      answer.push(scoreList.length - left);
    }
  });

  return answer;
}
