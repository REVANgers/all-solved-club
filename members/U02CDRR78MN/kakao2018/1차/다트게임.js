function solution(dartResult) {
  const multi = {
    S: 1,
    D: 2,
    T: 3,
  };

  const digit = /[0-9]+/g;

  const digits = dartResult.match(digit).map((char) => +char);
  const symbols = dartResult.split(digit).slice(1);

  digits.forEach((digit, i) => {
    symbols[i].split("").forEach((symbol) => {
      if (multi[symbol]) {
        digits[i] = digits[i] ** multi[symbol];
        return;
      }

      if (symbol === "*") {
        if (digits[i - 1]) {
          digits[i - 1] *= 2;
        }

        digits[i] *= 2;
        return;
      }

      if (symbol === "#") {
        digits[i] *= -1;
      }
    });
  });

  return digits.reduce((acc, n) => acc + n);
}
