function solution(orders, course) {
	const resMap = new Map();
	const refine = orders.map((order) => {
		return order.split("").sort().join("");
	});
	refine.forEach((order) => {
		course.forEach((n) => {
			combination(resMap, order, "", n, 0, 0, n);
		});
	});
	const arr = Array.from(resMap);
	const a = course.map((n) => {
		return arr.filter((elem) => elem[0].length === n);
	});
	const max = a
		.map((elem) => {
			return elem.reduce((res, cur) => {
				return res > cur[1] ? res : cur[1];
			}, 0);
		})
		.map((n) => (n > 1 ? n : 0));
	const result = a
		.map((elem, idx) => {
			return elem
				.filter((cur) => cur[1] === max[idx])
				.map((elem) => {
					return elem[0];
				});
		})
		.flat()
		.sort();

	return result;
}
function combination(resMap, str, res, r, idx, depth, target) {
	if (r === 0) {
		if (res.length === target) {
			const frequency = resMap.get(res);
			resMap.set(res, (frequency ? frequency : 0) + 1);
		}
	} else if (depth === str.length) {
		return;
	} else {
		combination(resMap, str, res + str[idx], r - 1, idx + 1, depth + 1, target);
		combination(resMap, str, res, r, idx + 1, depth + 1, target);
	}
}
