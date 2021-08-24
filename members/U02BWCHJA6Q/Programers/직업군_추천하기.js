// https://programmers.co.kr/learn/courses/30/lessons/84325

function solution(table, languages, preference) {
  const preferenceMap = {};
  const totalScore = [];

  languages.forEach(
    (language, index) => (preferenceMap[language] = preference[index]),
  );

  table.forEach(string => {
    const [type, ...languages] = string.split(' ');
    let sum = 0;
    let score = 5;

    languages.forEach((language, index) => {
      if (preferenceMap[language]) {
        sum += preferenceMap[language] * (score - index);
      }
    });

    totalScore.push({ type, sum });
  });

  totalScore.sort((a, b) => {
    if (a.sum !== b.sum) {
      return b.sum - a.sum;
    }

    return a.type < b.type ? -1 : 1;
  });

  return totalScore[0].type;
}
