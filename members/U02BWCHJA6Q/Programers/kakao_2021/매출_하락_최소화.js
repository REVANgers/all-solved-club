function solution(sales, links) {
  const teams = new Map();

  links.forEach(([leader, sub]) => {
    if (teams.has(leader)) {
      teams.get(leader).push(sub);

      return;
    }

    teams.set(leader, [sub]);
  });

  // dp[i][0] 루트인 i번 노드가 불참할 때 최소 값
  // dp[i][1] 루트인 i번 노드가 참여할 때 최소 값
  const dp = Array.from(Array(sales.length + 1), () => Array(2).fill(0));

  const dfs = (root) => {
    const sale = sales[root - 1];

    let sumChild = 0;
    let isMinSubRoot = false;
    const children = teams.get(root);

    if (!children) {
      dp[root][0] = 0;
      dp[root][1] = sale;

      return 0;
    }

    children.forEach((subRoot) => {
      sumChild += dfs(subRoot);

      if (dp[subRoot][0] > dp[subRoot][1]) {
        isMinSubRoot = true;
      }
    });

    dp[root][1] = sale + sumChild;
    dp[root][0] = sumChild;

    if (!isMinSubRoot) {
      let minDifferent = Infinity;

      children.forEach((subRoot) => {
        minDifferent = Math.min(minDifferent, dp[subRoot][1] - dp[subRoot][0]);
      });

      dp[root][0] += minDifferent;
    }

    return Math.min(dp[root][0], dp[root][1]);
  };

  return dfs(1);
}
