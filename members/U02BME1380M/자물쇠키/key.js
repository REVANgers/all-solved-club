function solution(key, lock) {
	const keys = [key];
	for (let i = 1; i < 4; i++) {
		keys.push(rotation(keys[i - 1]));
	}
	for (const rotKey of keys) {
		// 가능한 수 모두 대입
		for (let _y = -key.length; _y < lock.length + key.length; _y++) {
			for (let _x = -key.length; _x < lock.length + key.length; _x++) {
				// checker 를 통해서 loop 빠져나옴
				let checker = false;
				// lock에 대해서 대입을 위한 루프
				for (let y = 0; y < lock.length; y++) {
					for (let x = 0; x < lock.length; x++) {
						// k = 해당 자리에 해당되는 key
						let k = 0;
						// Boundary condition
						if (y - _y < 0 || y - _y >= key.length || x - _x < 0 || x - _x >= key.length) {
							k = 0;
						} else {
							k = rotKey[y - _y][x - _x];
						}
						// 끼웠을 때 상태
						let status = lock[y][x] + k;
						if (status !== 1) {
							checker = true;
						}
					}
					if (checker) {
						break;
					}
				}
				// checker 가 발동하지 않을 경우, 모두 1인 상황이다.
				if (!checker) return true;
			}
		}
	}
	return false;
}
function rotation(mat) {
	const result = [];
	const L = mat.length / 2;
	for (let i = 0; i < mat.length; i++) {
		result.push(Array(mat.length));
	}
	for (let l = 0; l < L; l++) {
		// case 1
		for (let i = 0; i < mat.length - 2 * l; i++) {
			result[i + l][mat.length - 1 - l] = mat[0 + l][i + l];
		}
		// case 2
		for (let i = 0; i < mat.length - 2 * l; i++) {
			result[mat.length - 1 - l][mat.length - 1 - i - l] = mat[i + l][mat.length - 1 - l];
		}
		// case 3
		for (let i = 0; i < mat.length - 2 * l; i++) {
			result[i + l][0 + l] = mat[mat.length - 1 - l][i + l];
		}
		// case 4
		for (let i = 0; i < mat.length - 2 * l; i++) {
			result[0 + l][i + l] = mat[mat.length - 1 - i - l][0 + l];
		}
	}
	return result;
}

console.log(
	solution(
		[
			[0, 0, 0],
			[1, 1, 0],
			[1, 1, 0],
		],
		[
			[1, 1, 1],
			[1, 1, 1],
			[1, 0, 1],
		]
	)
);
