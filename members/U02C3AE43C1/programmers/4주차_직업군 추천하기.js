function solution(table, languages, preference) {
  table = table.sort().map((row) => row.split(' ').reverse());
  const score = table.map((row) =>
    languages.reduce((acc, lang, idx) => acc + (row.indexOf(lang) + 1) * preference[idx], 0)
  );

  return table[score.indexOf(Math.max(...score))].pop();
}
