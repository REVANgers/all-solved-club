const map = {
	0: 0,
	A: 1,
	E: 2,
	I: 3,
	O: 4,
	U: 5,
};
function solution(word) {
	return [...Array(5)]
		.map((elem, idx) => (word[idx] ? map[word[idx]] : 0))
		.reduce((acc, cur, idx) => {
			return acc + (cur ? cur - 1 : 0) * remain(4 - idx) + (cur ? 1 : 0);
		}, 0);
}
const remain = (digits) => {
	if (digits === 0) {
		return 1;
	} else {
		return 1 + 5 * remain(digits - 1);
	}
};
