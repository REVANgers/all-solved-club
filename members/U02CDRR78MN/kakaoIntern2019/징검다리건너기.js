function solution(stones, k) {
  let left = 1;
  let right = 200000000;

  const possible = (num) => {
    let dangerous = 0;

    for (const stone of stones) {
      if (stone >= num) {
        dangerous = 0;
      } else {
        dangerous += 1;
      }

      if (dangerous === k) {
        return false;
      }
    }
    return true;
  };

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (possible(mid)) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return right;
}
