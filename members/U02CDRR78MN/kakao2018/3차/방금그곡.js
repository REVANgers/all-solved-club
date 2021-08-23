function solution(m, musicinfos) {
  // helpers
  const scaleRegex = /[A-G](#?)/g;
  const typedScale = (scale) => {
    if (scale.slice(-1) === "#") {
      return scale[0].toLowerCase();
    }

    return scale;
  };
  const hhmmToMinute = (hhmm) => +hhmm.slice(0, 2) * 60 + +hhmm.slice(3);

  const typedM = m.match(scaleRegex).map(typedScale).join("");

  const matched = musicinfos
    .map((musicInfo, i) => {
      let [start, end, title, scales] = musicInfo.split(",");
      scales = scales.match(scaleRegex).map(typedScale).join("");

      const scaleCount = hhmmToMinute(end) - hhmmToMinute(start);

      const q = Math.floor(scaleCount / scales.length);
      const r = scaleCount % scales.length;

      const song = scales.repeat(q) + scales.slice(0, r);
      const startIdx = song.indexOf(typedM);
      if (startIdx === -1) {
        return false;
      }

      return [title, scaleCount, i];
    })
    .filter((matched) => Boolean(matched));

  const compare = (a, b) =>
    b[1] > a[1] ? 1 : b[1] < a[1] ? -1 : b[2] > a[2] ? -1 : b[2] < a[2] ? 1 : 0;

  return matched.length ? matched.sort(compare)[0][0] : "(None)";
}
