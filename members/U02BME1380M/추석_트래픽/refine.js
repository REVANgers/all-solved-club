function solution(lines) {
	const MAX = 23 * 3600 * 1000 + 59 * 60 * 1000 + 59.999 * 1000;

	const REG = new RegExp("2016-09-15 (?<hour>[0-9]{2}):(?<min>[0-9]{2}):(?<sec>[0-9]{2}.[0-9]{3}) (?<dur>[0-9.]*)s");

	const verify = new Set();
	const list = [];

	lines.forEach((line) => {
		// law line을 크게 나눔
		const grouped = line.match(REG).groups;
		const [h, m, s, sec] = [grouped.hour, grouped.min, grouped.sec, grouped.dur];
		// 응답 완료시간, 요청 시간을 정수로 저장함.
		const e_time = h * 3600 * 1000 + m * 60 * 1000 + s * 1000;
		const s_time = e_time - sec * 1000 + 1;
		// BOUNDARY
		if (s_time < -2999 || e_time > MAX || s_time > MAX || e_time < 0) return;
		// 시각 데이터 기록
		list.push({ s_time: s_time, e_time: e_time });
		// 추후 검증을 위해 시각 기록
		if (s_time >= 0) {
			verify.add(s_time);
		}
		if (e_time <= MAX) {
			verify.add(e_time);
		}
	});
	let max = 0;
	for (const time of verify) {
		const filtered = list.filter((elem) => (time <= elem.s_time && elem.s_time <= time + 999) || (elem.s_time <= time && time <= elem.e_time) || (time <= elem.e_time && elem.e_time <= time + 999));
		if (filtered.length > max) {
			max = filtered.length;
		}
		//console.log(time,filtered);
	}
	return max;
}

// s_time, e_time 두 개를 기록해야한다.
// s_time, e_time 은 정수로 표현하는 것이 바람직하다.
// h * 3600 * 1000ms, m * 60 * 1000ms, s* 1000ms

// [s_time, e_time]을 가진 배열의 배열로 저장 및, s_time, e_time을 Set() 구조로 저장하여 s_time, e_time 별로 검증?
// 최대 2n^2 만큼 소요된다...
