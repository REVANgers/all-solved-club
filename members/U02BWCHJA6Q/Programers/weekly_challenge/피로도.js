function solution(k, dungeons) {
  let max = -1;

  const dfs = (k, remains, count) => {
    if (remains.length === 0) {
      max = Math.max(max, count);

      return;
    }

    for (let i = 0; i < remains.length; i++) {
      if (k >= remains[i][0] && k >= remains[i][1]) {
        dfs(
          k - remains[i][1],
          remains.filter((v, index) => index !== i),
          count + 1
        );
      } else {
        max = Math.max(max, count);
      }
    }
  };

  dfs(k, dungeons, 0);

  return max;
}
