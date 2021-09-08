function solution(m, n, board) {
	board = board.map((elem) => elem.split(""));
	let result = [];
	do {
		result = pang(m, n, board);
		if (result.length === 0) break;
		board = drop(m, n, toZero(board, result));
	} while (1);
	return board.reduce((result, elem) => {
		return (
			result +
			elem.reduce((res, cur) => {
				return res + (cur === 0 ? 1 : 0);
			}, 0)
		);
	}, 0);
}
function pang(m, n, board) {
	const result = [];
	for (let i = 0; i < m - 1; i++) {
		for (let j = 0; j < n - 1; j++) {
			const target = board[i][j];
			if (target && board[i][j + 1] === target && board[i + 1][j] === target && board[i + 1][j + 1] === target) {
				result.push([i, j]);
			}
		}
	}
	return result;
}
function toZero(board, pang) {
	const result = Array.from(board);
	pang.forEach((element) => {
		const i = element[0];
		const j = element[1];
		result[i][j] = 0;
		result[i][j + 1] = 0;
		result[i + 1][j] = 0;
		result[i + 1][j + 1] = 0;
	});
	return result;
}
function drop(m, n, board) {
	const result = Array.from(board);
	for (let i = 0; i < n; i++) {
		const cols = result.map((elem) => elem[i]);
		const res = [];
		cols.forEach((elem) => {
			if (elem) {
				res.push(elem);
			} else {
				res.unshift(0);
			}
		});
		res.forEach((elem, idx) => {
			result[idx][i] = elem;
		});
	}
	return result;
}
