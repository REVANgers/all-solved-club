function solution(cacheSize, cities) {
  var answer = 0;

  const set = new Set();

  if (cacheSize === 0) {
    return 5 * cities.length;
  }

  cities.forEach((city) => {
    const _city = city.toUpperCase();

    if (set.has(_city)) {
      answer += 1;
      set.delete(_city);
      set.add(_city);
      return;
    }

    if (cacheSize === set.size) {
      set.delete(set.keys().next().value);
    }

    answer += 5;
    set.add(_city);
  });

  return answer;
}
