const findParent = (parent, x) => {
  if (parent[x] !== x) {
    parent[x] = findParent(parent, parent[x]);
  }

  return parent[x];
};

const unionParent = (parent, a, b) => {
  a = findParent(parent, a);
  b = findParent(parent, b);

  if (a < b) {
    parent[b] = a;
  } else {
    parent[a] = b;
  }
};

function solution(n, wires) {
  let min = 100;

  wires.forEach((wire, index) => {
    const nextWires = wires.filter((_, i) => i !== index);
    const parent = Array(n + 1);
    const count = {};

    for (let i = 0; i <= n; i++) {
      parent[i] = i;
    }

    nextWires.forEach(([a, b]) => unionParent(parent, a, b));

    for (let i = 1; i <= n; i++) {
      const rootParent = findParent(parent, i);

      !count[rootParent] ? (count[rootParent] = 1) : count[rootParent]++;
    }

    const result = Object.values(count).reduce((acc, cur) =>
      Math.abs(acc - cur),
    );
    min = Math.min(min, result);
  });

  return min;
}
