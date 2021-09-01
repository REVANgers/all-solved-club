const alpha = ["A", "E", "I", "O", "U"];
const dict = {};
let order = 0;

const dfs = (cnt, word) => {
  if (cnt === 5) return;

  for (let i = 0; i < 5; i++) {
    dict[word + alpha[i]] = ++order;
    dfs(cnt + 1, word + alpha[i]);
  }
};

function solution(word) {
  dfs(0, "");
  return dict[word];
}
