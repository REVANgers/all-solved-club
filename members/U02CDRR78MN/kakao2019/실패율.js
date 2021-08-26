function solution(N, stages) {
  const staged = Array(N + 2).fill(0);

  stages.forEach((stage) => {
    staged[stage] += 1;
  });

  const allClear = staged[N + 1];

  let total = allClear;

  const failures = [];

  for (let i = N; i >= 1; i--) {
    const players = staged[i];

    total += players;

    failures.push([players / total, i]);
  }

  return failures
    .sort((a, b) => (b[0] > a[0] ? 1 : b[0] < a[0] ? -1 : a[1] - b[1]))
    .map((f) => f[1]);
}
