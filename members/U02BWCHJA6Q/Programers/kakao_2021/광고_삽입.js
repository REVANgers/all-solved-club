// https://www.welcomekakao.com/learn/courses/30/lessons/72414

const getSecondTime = (hours, minutes, seconds) =>
  60 * 60 * Number(hours) + 60 * Number(minutes) + Number(seconds);

const getStringTimeFromSecondTime = second => {
  const hh = Math.floor(second / (60 * 60));
  const mm = Math.floor((second - hh * 60 * 60) / 60);
  const ss = second - hh * 60 * 60 - mm * 60;

  return `${hh < 10 ? '0' + hh : hh}:${mm < 10 ? '0' + mm : mm}:${
    ss < 10 ? '0' + ss : ss
  }`;
};

function solution(play_time, adv_time, logs) {
  const playSecondTime = getSecondTime(...play_time.split(':'));
  const advSecondTime = getSecondTime(...adv_time.split(':'));
  const times = Array(playSecondTime).fill(0);

  logs.forEach(log => {
    const [startTime, endTime] = log.split('-');

    const startSecondTime = getSecondTime(...startTime.split(':'));
    const endSecondTime = getSecondTime(...endTime.split(':'));

    times[startSecondTime]++;
    times[endSecondTime]--;
  });

  for (let i = 1; i < playSecondTime; i++) {
    times[i] += times[i - 1];
  }

  for (let i = 1; i < playSecondTime; i++) {
    times[i] += times[i - 1];
  }

  let sum = times[advSecondTime - 1];
  let start = 0;

  for (let i = advSecondTime - 1; i < playSecondTime; i++) {
    if (sum < times[i] - times[i - advSecondTime]) {
      sum = times[i] - times[i - advSecondTime];
      start = i - advSecondTime + 1;
    }
  }

  return getStringTimeFromSecondTime(start);
}
