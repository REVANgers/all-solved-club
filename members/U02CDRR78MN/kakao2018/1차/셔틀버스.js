function solution(n, t, m, timetable) {
  var answer = "";

  const hhmmToMinute = (hhmm) => {
    const [hh, mm] = hhmm.split(":");

    return +hh * 60 + +mm;
  };
  const minuteToHhmm = (minute) => {
    const hh = `${Math.floor(minute / 60)}`.padStart(2, "0");
    const mm = `${minute % 60}`.padStart(2, "0");

    return `${hh}:${mm}`;
  };

  const start = 540;

  const sorted = timetable.map(hhmmToMinute).sort((a, b) => a - b);

  const buses = Array(n)
    .fill(0)
    .map((bus) => m);
  const last = Array(n).fill(0);

  let busIndex = 0;

  sorted.forEach((minute) => {
    while (buses[busIndex] === 0 || start + busIndex * t < minute) {
      busIndex++;
    }

    if (buses[busIndex]) {
      buses[busIndex] -= 1;
      last[busIndex] = minute;
    }
  });

  const minuteToRide =
    buses[n - 1] === 0 ? last[n - 1] - 1 : start + (n - 1) * t;

  return minuteToHhmm(minuteToRide);
}
