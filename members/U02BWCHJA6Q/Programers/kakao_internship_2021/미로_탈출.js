function solution(n, start, end, roads, traps) {
  const MAX_TRAP_MASKING = 1 << (traps.length + 1);

  const adj = Array.from(Array(n + 1), () => ({ origin: [], reverse: [] }));

  roads.forEach(([from, to, time]) => {
    adj[from].origin.push({ to, time });
    adj[to].reverse.push({ to: from, time });
  });

  const times = Array.from(Array(MAX_TRAP_MASKING), () =>
    Array(n + 1).fill(Infinity)
  );

  const isTrapOn = (index, masking) => {
    if (!traps.includes(index)) {
      return false;
    }

    const bitOn = masking & (1 << traps.indexOf(index));

    return bitOn > 0;
  };

  const isOriginalDirect = (trapOnA, trapOnB) =>
    (trapOnA && trapOnB) || (!trapOnA && !trapOnB);

  const getNextMasking = (index, masking) => {
    let nextMasking = masking;

    if (traps.includes(index)) {
      nextMasking ^= 1 << traps.indexOf(index);
    }

    return nextMasking;
  };

  const q = [{ from: start, time: 0, masking: 1 << traps.length }];
  let min = Infinity;

  while (q.length > 0) {
    const { from, time, masking } = q.shift();

    if (from === end) {
      min = Math.min(min, time);

      continue;
    }

    if (min <= time) {
      continue;
    }

    const trapOnFrom = isTrapOn(from, masking);

    adj[from].origin.forEach(({ to, time: toTime }) => {
      const trapOnTo = isTrapOn(to, masking);

      if (!isOriginalDirect(trapOnFrom, trapOnTo)) {
        return;
      }

      const nextTime = time + toTime;

      if (times[masking][to] > nextTime) {
        times[masking][to] = nextTime;

        q.push({
          from: to,
          time: nextTime,
          masking: getNextMasking(to, masking),
        });
      }
    });

    adj[from].reverse.forEach(({ to, time: toTime }) => {
      const trapOnTo = isTrapOn(to, masking);

      if (isOriginalDirect(trapOnFrom, trapOnTo)) {
        return;
      }

      const nextTime = time + toTime;

      if (times[masking][to] > nextTime) {
        times[masking][to] = nextTime;

        q.push({
          from: to,
          time: nextTime,
          masking: getNextMasking(to, masking),
        });
      }
    });
  }

  return min;
}
