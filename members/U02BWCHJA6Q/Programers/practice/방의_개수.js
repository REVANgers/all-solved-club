function solution(arrows) {
  let answer = 0;
  const direct = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
  ];
  const visited = new Set();
  const lines = new Set();
  let y = 0;
  let x = 0;
  visited.add('0-0');

  arrows.forEach((arrow) => {
    const nextY = y + direct[arrow][0];
    const nextX = x + direct[arrow][1];

    const key = `${nextY}-${nextX}`;
    const line = `${y}-${x}-${nextY}-${nextX}`;

    if (lines.has(line)) {
      y = nextY;
      x = nextX;

      return;
    }

    if (visited.has(key)) {
      answer++;
    }

    if (arrow === 1) {
      const reverseY = y - 1;
      const reverseX = x;
      const reverseNextY = y;
      const reverseNextX = x + 1;

      const reverseLine = `${reverseY}-${reverseX}-${reverseNextY}-${reverseNextX}`;

      if (lines.has(reverseLine)) {
        answer++;
      }
    } else if (arrow === 3) {
      const reverseY = y + 1;
      const reverseX = x;
      const reverseNextY = y;
      const reverseNextX = x + 1;

      const reverseLine = `${reverseY}-${reverseX}-${reverseNextY}-${reverseNextX}`;

      if (lines.has(reverseLine)) {
        answer++;
      }
    } else if (arrow === 5) {
      const reverseY = y;
      const reverseX = x - 1;
      const reverseNextY = y + 1;
      const reverseNextX = x;

      const reverseLine = `${reverseY}-${reverseX}-${reverseNextY}-${reverseNextX}`;

      if (lines.has(reverseLine)) {
        answer++;
      }
    } else if (arrow === 7) {
      const reverseY = y;
      const reverseX = x - 1;
      const reverseNextY = y - 1;
      const reverseNextX = x;

      const reverseLine = `${reverseY}-${reverseX}-${reverseNextY}-${reverseNextX}`;

      if (lines.has(reverseLine)) {
        answer++;
      }
    }

    const reverseLine = `${nextY}-${nextX}-${y}-${x}`;

    visited.add(key);
    lines.add(line);
    lines.add(reverseLine);

    y = nextY;
    x = nextX;
  });

  return answer;
}
