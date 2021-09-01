const menus = {};
let checked = {};

function dfs(idx, tmp, order) {
  if (!checked[tmp] && tmp) {
    checked[tmp] = 1;
    menus[tmp] ? menus[tmp]++ : (menus[tmp] = 1);
  }

  if (idx === order.length) return;

  for (let i = idx; i < order.length; i++) {
    dfs(i + 1, tmp + order[i], order);
    dfs(i + 1, tmp, order);
  }
}

function solution(orders, course) {
  let answer = [];

  orders.forEach((e) => {
    checked = {};
    dfs(0, "", e.split("").sort().join(""));
  });

  const candi = {};
  Object.keys(menus).forEach((e) => {
    candi[e.length] = candi[e.length] || {};

    if ((candi[e.length].cnt || 0) < menus[e]) {
      candi[e.length].cnt = menus[e];
      candi[e.length].menu = [e];
    } else if (candi[e.length].cnt === menus[e]) {
      candi[e.length].menu.push(e);
    }
  });

  course.forEach((e) => {
    if (candi[e] && candi[e].cnt >= 2) {
      answer.push(...candi[e].menu);
    }
  });

  return answer.sort();
}
