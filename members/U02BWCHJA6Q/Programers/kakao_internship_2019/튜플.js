// https://programmers.co.kr/learn/courses/30/lessons/64065

function solution(s) {
  const set = new Set();

  s.slice(2, s.length - 2)
    .split('},{')
    .sort((a, b) => a.length - b.length)
    .forEach(s => s.split(',').forEach(number => set.add(Number(number))));

  return [...set];
}
