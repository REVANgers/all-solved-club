function solution(s) {
  const zipLength = [];

  for (let i = 0; i < s.length / 2; i++) {
    const arr = [[s.slice(0, i + 1), 1]];
    let str = s.slice(i + 1);

    while (str.length > 0) {
      const word = str.slice(0, i + 1);

      if (arr[0][0] === word) {
        arr[0][1] += 1;
      } else {
        arr.unshift([word, 1]);
      }

      str = str.slice(i + 1);
    }

    zipLength.push(
      arr
        .map((el) => (el[1] === 1 ? [el[0]] : el))
        .flat()
        .join('').length
    );
  }

  return Math.min(...zipLength);
}
