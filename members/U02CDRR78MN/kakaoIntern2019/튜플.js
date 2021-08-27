function solution(s) {
  return Array.from(
    s
      .slice(2, -2)
      .split("},{")
      .sort((a, b) => a.length - b.length)
      .map((str) => str.split(","))
      .reduce((acc, set) => {
        set.forEach((d) => !acc.has(+d) && acc.add(+d));
        return acc;
      }, new Set())
  );
}
