// https://programmers.co.kr/learn/courses/30/lessons/72413

const dikstra = (start, adj) => {
  const distance = Array(adj.length).fill(Infinity);
  const q = [start];

  distance[start] = 0;

  while (q.length > 0) {
    const current = q.shift();

    adj[current].forEach(({ to, cost }) => {
      if (distance[to] > distance[current] + cost) {
        distance[to] = distance[current] + cost;

        q.push(to);
      }
    });
  }

  return distance;
};

function solution(n, s, a, b, fares) {
  const adj = Array.from(Array(n + 1), () => Array());

  fares.forEach(([from, to, cost]) => {
    adj[from].push({ to, cost });
    adj[to].push({ to: from, cost });
  });

  const distinctFromS = dikstra(s, adj);
  const distinctFromA = dikstra(a, adj);
  const distinctFromB = dikstra(b, adj);

  let min = Infinity;

  for (let waypoint = 1; waypoint <= n; waypoint++) {
    let sum = 0;
    sum += distinctFromS[waypoint];
    sum += distinctFromA[waypoint];
    sum += distinctFromB[waypoint];

    if (min > sum) {
      min = sum;
    }
  }

  return min;
}
