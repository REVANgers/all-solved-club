function solution(str1, str2) {
	const [elem_str1, elem_str2] = [spliter(str1), spliter(str2)];
	const intersectSet = intersect(elem_str1, elem_str2);
	const numberOfIntersect = getNumberOfDuplicateSet(intersectSet, elem_str1, elem_str2);
	const numberOfUnion = getNumberOfUnion(numberOfIntersect, elem_str1, elem_str2);
	return numberOfUnion ? Math.floor((numberOfIntersect / numberOfUnion) * 65536) : 65536;
}

const spliter = (str) => {
	const arr1 = [...Array(str.length - 1)]
		.map((elem, idx) => {
			const a = str[idx].toLowerCase();
			const b = str[idx + 1].toLowerCase();
			return `${a}${b}`;
		})
		.filter((elem) => {
			return elem.match(/[a-z]{2}/) !== null;
		});
	return arr1;
};

const intersect = (arr1, arr2) => {
	const result = arr1.filter((elem) => {
		return arr2.includes(elem);
	});
	const set = new Set(result);
	return set;
};
const getNumberOfDuplicateSet = (intersect, arr1, arr2) => {
	const set = Array.from(intersect);
	return set.reduce((acc, cur) => {
		const l1 = arr1.filter((elem) => cur === elem).length;
		const l2 = arr2.filter((elem) => cur === elem).length;
		return acc + Math.min(l1, l2);
	}, 0);
};
const getNumberOfUnion = (numberOfIntersect, arr1, arr2) => {
	return arr1.length + arr2.length - numberOfIntersect;
};
