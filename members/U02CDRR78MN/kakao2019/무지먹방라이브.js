function solution(food_times, k) {
  const foodTimes = food_times
    .map((foodTime, i) => [foodTime, i])
    .sort((a, b) => b[0] - a[0]);

  const mins = new Set();
  let lastMin;

  while (foodTimes.length) {
    const size = foodTimes.length;
    const [minFood, idx] = foodTimes[size - 1];

    if (mins.has(minFood)) {
      foodTimes.pop();
      continue;
    }
    mins.add(minFood);

    const r = k % size;

    const diff = lastMin ? minFood - lastMin : minFood;

    if (k < diff * size) {
      return foodTimes.sort((a, b) => a[1] - b[1])[r][1] + 1;
    }

    k -= diff * size;

    lastMin = minFood;
    foodTimes.pop();
  }

  return -1;
}
