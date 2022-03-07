function solution(info, edges) {
  let maxSheeps = 0;

  const adj = Array.from(Array(info.length), () => []);

  edges.forEach(([from, to]) => adj[from].push(to));

  const dfs = (from, wolfCount, sheepCount, nextList) => {
    sheepCount += info[from] ^ 1;
    wolfCount += info[from];

    if (sheepCount <= wolfCount) {
      return;
    }

    if (maxSheeps < sheepCount) {
      console.log(from);
      maxSheeps = sheepCount;
    }

    nextList.forEach((next) => {
      dfs(next, wolfCount, sheepCount, [
        ...[...nextList].filter((v) => v !== next),
        ...adj[next],
      ]);
    });
  };

  dfs(0, 0, 0, adj[0]);

  return maxSheeps;
}
