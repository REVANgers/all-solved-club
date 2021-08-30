function solution(record) {
	const nickNameMap = new Map();
	const doCommand = (elems) => {
		const [command, uid, nickname] = elems;
		if (nickname) {
			nickNameMap.set(uid, nickname);
		}
	};
	const getString = (elems) => {
		const [command, uid, nickname] = elems;
		switch (command) {
			case "Enter": {
				const name = nickNameMap.get(uid, nickname);
				return `${name}님이 들어왔습니다.`;
			}
			case "Leave": {
				const name = nickNameMap.get(uid, nickname);
				return `${name}님이 나갔습니다.`;
			}
		}
	};
	const info = record.map((elem) => elem.split(" "));
	info.forEach((elems) => doCommand(elems));
	return info.map((elems) => getString(elems)).filter((elem) => elem);
}
