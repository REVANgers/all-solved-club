function solution(s) {
	let res = "";
	let answer = "";
	for (const c of s) {
		res += c;
		const converted = converter(res);
		if (converted !== undefined) {
			answer += converted;
			res = "";
		}
	}
	return +answer;
}
function converter(s) {
	const str = s.toLowerCase();
	switch (s) {
		case "one":
		case "1":
			return 1;
		case "two":
		case "2":
			return 2;
		case "three":
		case "3":
			return 3;
		case "four":
		case "4":
			return 4;
		case "five":
		case "5":
			return 5;
		case "six":
		case "6":
			return 6;
		case "seven":
		case "7":
			return 7;
		case "eight":
		case "8":
			return 8;
		case "nine":
		case "9":
			return 9;
		case "zero":
		case "0":
			return 0;
		default:
			return undefined;
	}
}
