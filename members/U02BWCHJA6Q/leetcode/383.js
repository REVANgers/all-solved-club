/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  const ransomNoteCount = {};
  const magazineCount = {};

  for (let i = 0; i < ransomNote.length; i++) {
    const c = ransomNote[i];

    !ransomNoteCount[c] ? (ransomNoteCount[c] = 1) : (ransomNoteCount[c] += 1);
  }

  for (let i = 0; i < magazine.length; i++) {
    const c = magazine[i];

    !magazineCount[c] ? (magazineCount[c] = 1) : (magazineCount[c] += 1);
  }

  return Object.entries(ransomNoteCount).every(
    ([key, value]) => value <= magazineCount[key],
  );
};
