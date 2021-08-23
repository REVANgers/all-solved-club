function solution(files) {
  var answer = [];

  const compare = (a, b) =>
    a.head < b.head ? -1 : a.head > b.head ? 1 : +a.number - +b.number;

  return files
    .map((file, i) => {
      const groups = file.match(
        /(?<head>[a-zA-Z\-\s]+)(?<number>[0-9]{1,5})(?<tail>.*)/
      ).groups;
      Object.keys(groups).forEach((key) => {
        groups[key] = groups[key].toUpperCase();
      });
      return [groups, i];
    })
    .sort((a, b) => compare(a[0], b[0]))
    .map(([groups, i]) => files[i]);
}
