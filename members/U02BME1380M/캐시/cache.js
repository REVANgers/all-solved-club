function solution(cacheSize, cities) {
	if (cacheSize === 0) return cities.length * 5;
	let caches = [];
	let answer = 0;
	cities.forEach((city) => {
		const cached = city.toLowerCase();
		if (caches.includes(cached)) {
			const idx = caches.indexOf(cached);
			caches.splice(idx, 1);
			answer += 1;
		} else {
			if (caches.length === cacheSize) {
				caches.shift();
			}
			answer += 5;
		}
		caches.push(cached);
	});
	return answer;
}
