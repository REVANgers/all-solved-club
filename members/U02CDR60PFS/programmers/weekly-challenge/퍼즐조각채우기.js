// 이게 js인가 c++인가 ㅋㅋㅋㅋㅋㅋㅋㅋ
const isInside = (x, y, len) => x >= 0 && x < len && y >= 0 && y < len;

function getBlocks(board) {
  const len = board.length;
  const visited = Array.from(Array(len), () => Array(len).fill(false));
  let blocks = [], block = [], startPos = [];

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (board[i][j] && !visited[i][j]) {
        visited[i][j] = true;
        startPos.push([j, i]);
        block.push([j, i]);
        dfs(j, i);
        blocks.push(block.map((e) => [e[0] - j, e[1] - i]));
        block = [];
      }
    }
  }

  function dfs(cx, cy) {
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];

    for (let i = 0; i < 4; i++) {
      let nx = cx + dx[i];
      let ny = cy + dy[i];

      if (isInside(nx, ny, len) && !visited[ny][nx] && board[ny][nx]) {
        visited[ny][nx] = true;
        block.push([nx, ny]);
        dfs(nx, ny);
      }
    }
  }
  return [blocks, startPos];
}

function rotate(board) {
  const len = board.length;
  const ret = Array.from(Array(len), () => Array(len).fill(0));

  for (let i = 0; i < len; i++)
    for (let j = 0; j < len; j++)
      ret[j][len - 1 - i] = board[i][j];
  return ret;
}

const markBoard = (board, block, startPos) => 
  block.forEach((e) => (board[e[1] + startPos[1]][e[0] + startPos[0]] = 0));

function solution(game_board, table) {
  let answer = 0;
  const [table_blocks, _] = getBlocks(table);
  let isUsed = [], isFilled = [];
  game_board = game_board.map((row) => row.map((e) => (e ? 0 : 1)));

  for (let t = 0; t < 4; t++) {
    const [board_blocks, startPos] = getBlocks(game_board);
    isFilled = [];
    for (let i = 0; i < table_blocks.length; i++) {
      if (!isUsed[i]) {
        for (let j = 0; j < board_blocks.length; j++) {
          if (
            !isFilled[j] &&
            JSON.stringify(table_blocks[i]) === JSON.stringify(board_blocks[j])
          ) {
            answer += table_blocks[i].length;
            isUsed[i] = true;
            isFilled[j] = true;
            markBoard(game_board, board_blocks[j], startPos[j]);
            break;
          }
        }
      }
    }
    game_board = rotate(game_board);
  }
  return answer;
}
