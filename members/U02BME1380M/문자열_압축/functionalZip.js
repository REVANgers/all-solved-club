function solution(s) {
	if (s.length < 2) return s.length;
	const range = [...Array(Math.floor(s.length / 2))];
	return range.map((_, i) => divider(s, i + 1).length).reduce((prev, cur) => (prev > cur ? cur : prev));
}

function divider(string, length) {
	const regex = new RegExp(`.{1,${length}}`, "g");
	const array = [...string.match(regex), ""];
	const make = ([result, pattern, count]) => `${result}${count ? count + 1 : ""}${pattern}`;
	return array.reduce(([result, pattern, count], cur) => (pattern === cur ? [result, pattern, count + 1] : [make([result, pattern, count]), cur, 0]), ["", "", 0])[0];
}
