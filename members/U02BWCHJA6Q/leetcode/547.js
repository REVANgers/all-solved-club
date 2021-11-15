/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
  const bfs = start => {
    const q = [start];

    while (q.length > 0) {
      const from = q.shift();

      adj[from].forEach(next => {
        if (visited[next]) {
          return;
        }

        visited[next] = true;
        q.push(next);
      });
    }
  };
  const adj = [];

  isConnected.forEach((numbers, i) => {
    const nodes = [];
    numbers.forEach((status, j) => {
      if (i !== j && status === 1) {
        nodes.push(j);
      }
    });
    adj.push(nodes);
  });

  const visited = Array(isConnected.length).fill(false);
  let count = 0;

  for (let i = 0; i < isConnected.length; i++) {
    if (!visited[i]) {
      visited[i] = true;
      bfs(i);
      count++;
    }
  }

  return count;
};
