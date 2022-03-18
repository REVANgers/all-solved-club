function solution(words, queries) {
  const answer = [];
  const map = new Map();
  const reverseMap = new Map();

  words.forEach((word) => {
    const length = word.length;

    if (map.has(length)) {
      map.get(length).push(word);
    } else {
      map.set(length, [word]);
    }

    const reverseWord = word.split('').reverse().join('');

    if (reverseMap.has(length)) {
      reverseMap.get(length).push(reverseWord);
    } else {
      reverseMap.set(length, [reverseWord]);
    }
  });

  [...map].forEach(([_, words]) => words.sort((a, b) => (a < b ? -1 : 1)));
  [...reverseMap].forEach(([_, reverseWords]) =>
    reverseWords.sort((a, b) => (a < b ? -1 : 1))
  );

  const getCount = (array, query) =>
    upperBound(array, query.replace(/\?/g, 'z')) -
    lowerBound(array, query.replace(/\?/g, 'a'));

  const lowerBound = (array, target) => {
    if (!array) {
      return 0;
    }

    let begin = 0;
    let end = array.length;

    while (begin <= end) {
      const mid = ((begin + end) / 2) | 0;

      if (array[mid] < target) {
        begin = mid + 1;
      } else {
        end = mid - 1;
      }
    }

    return end;
  };

  const upperBound = (array, target) => {
    if (!array) {
      return 0;
    }

    let begin = 0;
    let end = array.length;

    while (begin <= end) {
      const mid = ((begin + end) / 2) | 0;

      if (array[mid] <= target) {
        begin = mid + 1;
      } else {
        end = mid - 1;
      }
    }

    return end;
  };

  queries.forEach((query) => {
    let isReverse = false;

    if (query[0] === '?') {
      isReverse = true;
    }

    if (isReverse) {
      answer.push(
        getCount(
          reverseMap.get(query.length),
          query.split('').reverse().join('')
        )
      );
    } else {
      answer.push(getCount(map.get(query.length), query));
    }
  });

  return answer;
}
