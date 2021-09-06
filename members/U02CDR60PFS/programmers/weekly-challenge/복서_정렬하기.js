function solution(weights, head2head) {
  const result = [];

  weights.forEach((e, i) => (result[i] = { id: i + 1, weight: e }));

  head2head.forEach((op, i) => {
    let win = 0,
      lose = 0,
      cnt = 0;
    op.split("").forEach((res, j) => {
      if (res == "W") {
        ++win;
        if (weights[i] < weights[j]) ++cnt;
      }
      if (res == "L") ++lose;
    });
    const rate = win + lose === 0 ? 0 : win / (win + lose);
    result[i].rate = rate;
    result[i].cnt = cnt;
  });

  return result
    .sort(
      (a, b) =>
        b.rate - a.rate || b.cnt - a.cnt || b.weight - a.weight || a.id - b.id
    )
    .map((e) => e.id);
}
