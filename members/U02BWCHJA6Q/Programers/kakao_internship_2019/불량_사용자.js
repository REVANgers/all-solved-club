// https://programmers.co.kr/learn/courses/30/lessons/64064

const set = new Set();

const dfs = (bannedList, index, result) => {
  if (bannedList.length === index) {
    set.add(result.sort().join(''));

    return;
  }

  bannedList[index].forEach(current => {
    if (result.includes(current)) {
      return;
    }

    dfs(bannedList, index + 1, [...result, current]);
  });
};

function solution(user_id, banned_id) {
  const bannedList = [];

  banned_id.forEach(bannedId => {
    const list = [];
    const regex = new RegExp(bannedId.replace(/\*/g, '.'));

    user_id.forEach(userId => {
      if (userId.length !== bannedId.length) {
        return;
      }
      const matched = userId.match(regex);

      if (matched) {
        list.push(matched[0]);
      }
    });

    bannedList.push(list);
  });

  dfs(bannedList, 0, []);

  return set.size;
}
