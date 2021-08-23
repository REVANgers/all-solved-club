function solution(lines) {
  var answer = 0;

  const startEnd = [];

  lines.map((line) => {
    const [yyyymmdd, hhmmss, duration] = line.split(" ");

    const [year, month, date] = yyyymmdd.split("-");
    const [hh, mm, ss] = hhmmss.split(":");

    const end =
      new Date(year, month, date, hh, mm, +ss.slice(0, 2)).getTime() +
      +ss.slice(3);
    const start = end - +duration.slice(0, -1) * 1000 - 999;

    startEnd.push([start, "start"], [end, "end"]);
  });

  let count = 0;

  startEnd
    .sort((a, b) => a[0] - b[0])
    .forEach((time) => {
      count += time[1] === "start" ? 1 : -1;

      answer = Math.max(answer, count);
    });

  return answer;
}

/*
    new Date('yyyy-mm-dd hh:mm:ss.sss')로 날짜 객체를 생성할 수 있다.
*/
