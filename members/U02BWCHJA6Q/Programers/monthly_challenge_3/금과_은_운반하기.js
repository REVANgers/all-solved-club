function solution(a, b, g, s, w, t) {
  let left = 0;
  let right = 1000000000000000 * 2;
  let answer = right;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    let totalMaxResource = 0;
    let totalMaxGold = 0;
    let totalMaxSilver = 0;

    for (let i = 0; i < t.length; i++) {
      const count = Math.floor((mid / t[i] + 1) / 2);
      const maxResource = Math.min(g[i] + s[i], w[i] * count);

      totalMaxGold += Math.min(g[i], maxResource);
      totalMaxSilver += Math.min(s[i], maxResource);
      totalMaxResource += maxResource;
    }

    if (totalMaxResource >= a + b && totalMaxGold >= a && totalMaxSilver >= b) {
      answer = Math.min(answer, mid);
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return answer;
}
