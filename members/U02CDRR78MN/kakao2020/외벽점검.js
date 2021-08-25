function solution(n, weak, dist) {
  var answer = 0;

  const weaks = weak.map((w, i) => [
    ...weak.slice(i),
    ...weak.slice(0, i).map((w) => w + n),
  ]);

  const permutation = (arr) => {
    if (arr.length === 1) {
      return [arr];
    }

    const res = [];

    arr.forEach((picked, i) => {
      permutation([...arr.slice(0, i), ...arr.slice(i + 1)]).forEach(
        (smaller) => {
          res.push([picked, ...smaller]);
        }
      );
    });

    return res;
  };

  const dists = permutation(dist);

  let min = Infinity;

  weaks.forEach((weak) => {
    dists.forEach((dist) => {
      let start = 0;
      let current = 1;

      for (let i = 0; i < dist.length; i++) {
        const d = dist[i];

        while (weak[current] - weak[start] <= d) {
          current++;

          if (current === weaks.length) {
            min = Math.min(min, i + 1);
            return;
          }
        }

        start = current;
      }
    });
  });

  return min === Infinity ? -1 : min;
}
