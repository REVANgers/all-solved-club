function solution(record) {
  const users = {};

  return record
    .map((rec) => rec.split(" "))
    .filter(([event, userId, payload]) => {
      if (event === "Change") {
        users[userId] = payload;
        return false;
      }

      if (event === "Enter") {
        users[userId] = payload;
      }

      return true;
    })
    .map(([event, userId]) =>
      event[0] === "E"
        ? `${users[userId]}님이 들어왔습니다.`
        : `${users[userId]}님이 나갔습니다.`
    );
}
