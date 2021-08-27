function solution(user_id, banned_id) {
  var answer = 0;

  const hash = user_id.reduce((acc, key, id) => acc.set(key, id), new Map());

  const users = user_id.join(",");
  const banned = banned_id.map((b) =>
    users.match(new RegExp(`${b.replace(/\*/g, `[0-9a-z]{1}`)}`, "g"))
  );

  const bannedSet = new Set();

  const dfs = (banned, depth, bannedList = new Set()) => {
    if (depth === banned.length) {
      bannedSet.add(Array.from(bannedList).sort().join(""));
      return;
    }

    banned[depth].forEach((bannedKey) => {
      const bannedId = hash.get(bannedKey);
      if (bannedId === undefined) return;
      if (bannedList.has(bannedId)) return;

      const newBannedList = new Set(bannedList);
      newBannedList.add(bannedId);

      dfs(banned, depth + 1, newBannedList);
    });
  };

  dfs(banned, 0);

  return bannedSet.size;
}
