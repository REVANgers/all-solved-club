/*
좋지 않은 노가다 풀이
회전을 이용해서 풀고싶었는데 지울 수 있는 블락을 찾는 방법을 발견하지 못 했다.
*/
function solution(board) {
  var answer = 0;

  const blocks = [
    [
      [1, 0, 0],
      [1, 1, 1],
    ],
    [
      [0, 1, 0],
      [1, 1, 1],
    ],
    [
      [0, 0, 1],
      [1, 1, 1],
    ],
    [
      [1, 0],
      [1, 0],
      [1, 1],
    ],
    [
      [0, 1],
      [0, 1],
      [1, 1],
    ],
  ];

  const isUpperBlock = (x, y) => {
    for (let yy = 0; yy < y; yy++) {
      if (board[yy][x]) {
        return true;
      }
    }
    return false;
  };

  for (let y = 0; y < board.length - 1; y++) {
    for (let x = 0; x < board[0].length - 1; x++) {
      for (let i = 0; i < blocks.length; i++) {
        const block = blocks[i];

        if (
          y + block.length > board.length ||
          x + block[0].length > board[0].length
        ) {
          continue;
        }

        let color;
        const matched = block.every((row, r) =>
          row.every((b, c) => {
            const xx = x + c;
            const yy = y + r;

            if (!color && board[yy][xx]) {
              color = board[yy][xx];
            }

            return (!board[yy][xx] && !b) || board[yy][xx] === color;
          })
        );

        if (matched) {
          const zeros = block[0]
            .map((b, i) => [b, i])
            .filter((b) => b[0] === 0);
          if (zeros.every((zero) => !isUpperBlock(x + zero[1], y))) {
            answer++;

            block.forEach((row, r) =>
              row.forEach((b, c) => {
                board[y + r][x + c] = 0;
              })
            );

            x = 0;
          }
        }
      }
    }
  }

  return answer;
}
