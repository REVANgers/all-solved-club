// https://programmers.co.kr/learn/courses/30/lessons/42888

const COMMAND_MAP = Object.freeze({
  ENTER: 'Enter',
  CHANGE: 'Change',
  LEAVE: 'Leave',
});

function solution(record) {
  const answer = [];
  const userMap = {};
  const commandList = [];

  record.forEach(string => {
    const [command, id, nickName] = string.split(' ');

    if (command === COMMAND_MAP.CHANGE) {
      userMap[id] = nickName;

      return;
    }

    commandList.push({ command, id });

    if (command === COMMAND_MAP.ENTER) {
      userMap[id] = nickName;
    }
  });

  commandList.forEach(({ command, id }) => {
    command === COMMAND_MAP.ENTER
      ? answer.push(`${userMap[id]}님이 들어왔습니다.`)
      : answer.push(`${userMap[id]}님이 나갔습니다.`);
  });

  return answer;
}
