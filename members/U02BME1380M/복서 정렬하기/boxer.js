function solution(weights, head2head) {
	const boxers = Array.from(weights);
	const fightRes = boxers
		.map((boxer, i) => {
			// res : [W,GAME, SW] , SW : 체급이 더 높은 사람과의 승리 수
			const fights = head2head[i].split("");
			return fights.reduce(
				(res, fight, j) => {
					if (i === j || fight === "N") return res;
					const isHeavy = boxers[i] < boxers[j] ? 1 : 0;
					switch (fight) {
						case "W": {
							return [res[0] + 1, res[1] + 1, res[2] + isHeavy];
						}
						case "L": {
							return [res[0], res[1] + 1, res[2]];
						}
					}
				},
				[0, 0, 0]
			);
		})
		.map((res) => {
			if (res[1]) {
				return [res[0] / res[1], res[2]];
			} else {
				return [0, 0];
			}
		});
	const result = fightRes.sort((a, b) => {
		if (a[0] > b[0]) {
			return 1;
		} else if (a[0] === b[0]) {
			if (a[1] > b[1]) {
				return 1;
			} else if (a[1] === b[1]) {
				return 0;
			} else {
				return -1;
			}
		} else {
			return -1;
		}
	});

	return result;
}
