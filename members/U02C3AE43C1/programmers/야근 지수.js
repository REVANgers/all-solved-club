function solution(n, works) {
  const length = works.length;
  works.sort((a, b) => b - a);

  for (let i = 0; i < n; i++) {
    let num = works.shift();

    if (num > 0) {
      num -= 1;
    }

    for (let j = 0; j < works.length; j++) {
      if (works[j] <= num) {
        works.splice(j, 0, num);
        break;
      }
    }

    if (works.length !== length) {
      works.push(num);
    }
  }

  return works.reduce((acc, cur) => acc + cur ** 2, 0);
}
