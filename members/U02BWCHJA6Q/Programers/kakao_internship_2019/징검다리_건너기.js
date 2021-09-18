// https://programmers.co.kr/learn/courses/30/lessons/64062

function solution(stones, k) {
  let left = 0;
  let right = 200000000;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    const nextStones = stones.map(stone => stone - mid);
    let jump = 0;

    nextStones.some(stone => {
      if (jump === k) {
        return true;
      }

      stone > 0 ? (jump = 0) : jump++;
    });

    if (jump === k) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
}
