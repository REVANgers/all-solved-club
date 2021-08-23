function solution(str1, str2) {
  var answer = 0;

  const upperAlpha = /[A-Z]/g;

  const getSet = (str) => {
    const set = {};

    for (let i = 0; i < str.length - 1; i++) {
      const subStr = str.slice(i, i + 2);
      const alphas = subStr.match(upperAlpha);

      if (alphas && alphas.length === 2) {
        set[subStr] = ++set[subStr] || 1;
      }
    }

    return set;
  };

  const sum = (set1, set2) => {
    const set = { ...set1 };

    Object.entries(set2).forEach(([key, value]) => {
      set[key] = set[key] ? Math.max(set[key], value) : value;
    });

    return set;
  };

  const intersect = (set1, set2) => {
    const set = {};

    Object.entries(set2).forEach(([key, value]) => {
      if (set1[key]) {
        set[key] = Math.min(set1[key], value);
      }
    });
    Object.entries(set1).forEach(([key, value]) => {
      if (set2[key]) {
        set[key] = Math.min(set2[key], value);
      }
    });

    return set;
  };

  const smilarityFactor = (str1, str2) => {
    const set1 = getSet(str1);
    const set2 = getSet(str2);

    const intersectValues = Object.values(intersect(set1, set2));
    const sumValues = Object.values(sum(set1, set2));

    if (sumValues.length === 0) {
      return 1;
    }

    const factor =
      intersectValues.reduce((acc, _) => acc + _, 0) /
      sumValues.reduce((acc, _) => acc + _, 0);

    return factor;
  };

  return Math.floor(
    smilarityFactor(str1.toUpperCase(), str2.toUpperCase()) * 65536
  );
}
