const solution = (price, money, count) =>
  Math.max(0, (price * count * (count + 1)) / 2 - money);
