function solution(lottos, win_nums) {
	const answer = lottos
		.reduce(
			(result, number) => {
				if (number === 0) {
					return [result[0], result[1] + 1];
				}
				if (win_nums.includes(number)) {
					return [result[0] + 1, result[1] + 1];
				} else {
					return result;
				}
			},
			[0, 0]
		)
		.map((corrects) => {
			const res = [6, 6, 5, 4, 3, 2, 1];
			return res[corrects];
		})
		.reverse();
	return answer;
}
