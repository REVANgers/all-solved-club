function solution(n, t, m, p) {
  let str = "";
  let count = 0;

  while (str.length < p + (t - 1) * m) {
    str += count.toString(n).toUpperCase();
    count++;
  }

  return str
    .split("")
    .filter((char, i) => i % m === p - 1)
    .slice(0, t)
    .join("");
}
