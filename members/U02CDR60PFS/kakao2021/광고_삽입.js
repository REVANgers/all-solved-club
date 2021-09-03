function solution(play_time, adv_time, logs) {
  const calcTime = (t) => {
    t = t.split(":");
    return t[0] * 3600 + t[1] * 60 + t[2] * 1;
  };

  const formatTime = (t) => {
    let hh = parseInt(t / 3600);
    let mm = parseInt((t %= 3600) / 60);
    let ss = t % 60;

    hh = hh < 10 ? "0" + hh : hh;
    mm = mm < 10 ? "0" + mm : mm;
    ss = ss < 10 ? "0" + ss : ss;
    return `${hh}:${mm}:${ss}`;
  };

  play_time = calcTime(play_time);
  adv_time = calcTime(adv_time);
  let answer = 0;
  const timeLine = Array.from({ length: play_time + 1 }, () => 0);

  logs
    .map((log) => log.split("-").map((el) => calcTime(el)))
    .forEach((e) => {
      timeLine[e[0]]++;
      timeLine[e[1]]--;
    });

  const accTime = [timeLine[0]];
  for (let i = 1; i < play_time; i++) {
    timeLine[i] += timeLine[i - 1];
    accTime[i] = timeLine[i] + accTime[i - 1];
  }

  // accTime의 i-1번째 인덱스를 접근해야해서 i를 1부터 했더니 광고 시작 시간이 0인 경우가 고려되지 않음
  // 따라서 i를 0부터 하고 accTime[i-1] || 0 와 같이 단축 평가를 사용
  let maxPlayTime = 0;
  for (let i = 0; i <= play_time - adv_time; i++) {
    const pt = accTime[i + adv_time - 1] - (accTime[i - 1] || 0);
    if (pt > maxPlayTime) {
      maxPlayTime = pt;
      answer = i;
    }
  }
  return formatTime(answer);
}
