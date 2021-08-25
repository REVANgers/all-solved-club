function solution(s) {
  if (s.length === 1) {
    return 1;
  }

  const compress = (remains, n) => {
    const stack = [[remains.slice(0, n), 1]];

    for (let i = n; i < remains.length; i += n) {
      const [prev, count] = stack.pop();
      const next = remains.slice(i, i + n);

      prev === next
        ? stack.push([prev, count + 1])
        : stack.push([prev, count], [next, 1]);
    }

    return stack.map((s) => (s[1] === 1 ? s[0] : s[1] + s[0])).join("");
  };

  const size = s.length;

  let min = Infinity;
  let ratio = 1;

  while (ratio <= size / 2) {
    const compressed = compress(s, ratio);

    min = Math.min(compressed.length, min);

    ratio++;
  }

  return min;
}
