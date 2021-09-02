function solution(info, query) {
  let answer = [];
  const infos = {};

  info = info.map((e) => {
    e = e.split(" ");
    const score = e.pop() * 1;
    dfs(0, []);

    function dfs(idx, info) {
      const key = info.join("");
      infos[key] = infos[key] || [];
      infos[key].push(score);

      for (let i = idx; i < e.length; i++) {
        info.push(e[i]);
        dfs(i + 1, info);
        info.pop();
      }
    }
  });

  Object.keys(infos).forEach((e) => infos[e].sort((a, b) => a - b));

  query.forEach((q) => {
    q = q.split(" ");
    const score = q.pop();
    q = q.filter((e) => e !== "-" && e !== "and").join("");
    if (!infos[q]) {
      answer.push(0);
      return;
    }

    let cnt = binarySearch(0, infos[q].length, score);
    answer.push(cnt);

    function binarySearch(left, right, target) {
      while (left < right) {
        let mid = parseInt((left + right) / 2);
        if (infos[q][mid] < target) {
          left = mid + 1;
        } else if (infos[q][mid] >= target) {
          right = mid;
        }
      }
      return infos[q].length - left;
    }
  });
  return answer;
}
