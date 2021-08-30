function solution(s) {
	let answer = s.length;
	const length = s.length;
	for (let i = 1; i <= length / 2; i++) {
		const l = divider(s, i);
		answer = answer > l ? l : answer;
	}
	return answer;
}

function divider(string, length) {
	const regex = new RegExp(`.{${length}}`, "g");
	const array = string.match(regex);
	let prev = "";
	let counter = 0;
	let compressed = 0;
	for (const s of array) {
		if (prev === s) {
			counter++;
		} else {
			compressed += getCompressed(counter, length);
			prev = s;
			counter = 0;
		}
	}
	compressed += getCompressed(counter, length);
	return string.length - compressed;
}
function getCompressed(counter, length) {
	return counter ? counter * length - Math.floor(Math.log10(counter + 1) + 1) : 0;
}
