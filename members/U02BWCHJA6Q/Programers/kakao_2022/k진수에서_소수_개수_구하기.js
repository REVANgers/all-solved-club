function solution(n, k) {
  const isPrime = (n) => {
    if (n === 1) {
      return false;
    }

    if (n === 2) {
      return true;
    }

    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }

    return true;
  };

  return n
    .toString(k)
    .split('0')
    .filter((s) => {
      if (!s) {
        return false;
      }

      return isPrime(Number(s));
    }).length;
}
