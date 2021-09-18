function solution(skill, skill_trees) {
	const skills = skill.split("");
	const s_trees = skill_trees.map((elem) => elem.split(""));
	const result = s_trees.map((elem) => {
		const intersect = elem.filter((cur) => skills.includes(cur));
		const idx = intersect.map((cur) => skills.indexOf(cur));
		let prev = 0;
		for (const n of idx) {
			if (prev !== n) return 0;
			prev++;
		}
		return 1;
	});
	return result.reduce((res, cur) => res + cur);
}
