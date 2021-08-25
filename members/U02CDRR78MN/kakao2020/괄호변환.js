// 생각 없이 시키는대로 짜면 풀리는 문제..?

function solution(p) {
  const transform = (unpair) => {
    if (unpair === "") {
      return "";
    }

    let count = 0;
    let balanced = "";

    for (let i = 0; i < unpair.length; i++) {
      unpair[i] === "(" ? count++ : count--;

      balanced += unpair[i];

      if (count === 0) {
        const u = balanced;
        const v = unpair.slice(i + 1);

        return unpair[0] === "("
          ? u + transform(v)
          : `(${transform(v)})${u
              .slice(1, -1)
              .split("")
              .map((c) => (c === ")" ? "(" : ")"))
              .join("")}`;
      }
    }
  };

  return transform(p);
}
