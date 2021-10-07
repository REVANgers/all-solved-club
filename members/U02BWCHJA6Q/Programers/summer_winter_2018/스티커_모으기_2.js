function solution(sticker) {
  if (sticker.length === 1) {
    return sticker[0];
  }

  const dp1 = Array(sticker.length + 2).fill(0);
  const dp2 = Array(sticker.length + 2).fill(0);

  for (let i = 2; i < sticker.length + 2 - 1; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + sticker[i - 2]);
  }

  for (let i = 3; i < sticker.length + 2; i++) {
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i - 2]);
  }

  return Math.max(dp1[dp1.length - 2], dp2[dp2.length - 1]);
}
