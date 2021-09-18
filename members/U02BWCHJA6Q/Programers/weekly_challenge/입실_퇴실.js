function solution(enter, leave) {
  const meeted = Array.from(Array(enter.length), () => new Set());
  const out = new Set();

  leave.forEach(leavedNumber => {
    const index = enter.indexOf(leavedNumber);
    const meetedNumbers = [];

    for (let i = 0; i <= index; i++) {
      const enteredNumber = enter[i];

      if (!out.has(enteredNumber)) {
        meetedNumbers.push(enteredNumber);
      }
    }

    if (meetedNumbers.length > 1) {
      meetedNumbers.forEach(number => {
        for (let current of meetedNumbers) {
          if (number != current) {
            meeted[current - 1].add(number);
          }
        }
      });
    }

    out.add(leavedNumber);
  });

  return meeted.map(set => [...set].length);
}
