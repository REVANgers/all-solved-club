function calDiff(cur, visited, wires) {
  visited[cur - 1] = true;

  wires.forEach((wire) => {
    if (wire[0] === cur && !visited[wire[1] - 1]) {
      calDiff(wire[1], visited, wires);
    } else if (wire[1] === cur && !visited[wire[0] - 1]) {
      calDiff(wire[0], visited, wires);
    }
  });

  return Math.abs(visited.filter((el) => el).length - visited.filter((el) => !el).length);
}

function solution(n, wires) {
  let answer = 100;

  wires.forEach((wire, idx) => {
    const newWires = [...wires];
    newWires.splice(idx, 1);
    const diff = calDiff(1, new Array(n).fill(false), newWires);

    if (answer > diff) {
      answer = diff;
    }
  });

  return answer;
}
