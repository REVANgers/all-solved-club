function solution(fees, records) {
  const [BASIC_TIME, BASIC_FEE, STANDARD_TIME, STANDARD_FEE] = fees;

  const TYPE = {
    IN: 'IN',
    OUT: 'OUT',
  };
  const LAST_TIME = '23:59';
  const informationMap = new Map();

  const getSecondTimeFromString = (string) => {
    const [hours, seconds] = string.split(':');

    return Number(hours) * 60 + Number(seconds);
  };

  records.forEach((string) => {
    const [timeString, id, type] = string.split(' ');

    if (!informationMap.has(id)) {
      informationMap.set(id, [{ timeString, type }]);

      return;
    }

    informationMap.get(id).push({ timeString, type });
  });

  return [...informationMap]
    .map(([id, information]) => {
      let totalTimes = 0;

      for (let i = 0; i < information.length; i += 2) {
        const inTime = getSecondTimeFromString(information[i].timeString);
        const outTime = information[i + 1]
          ? getSecondTimeFromString(information[i + 1].timeString)
          : getSecondTimeFromString(LAST_TIME);

        totalTimes += outTime - inTime;
      }

      let plusFees = 0;
      if (totalTimes > BASIC_TIME) {
        plusFees =
          Math.ceil((totalTimes - BASIC_TIME) / STANDARD_TIME) * STANDARD_FEE;
      }

      return { id, fee: BASIC_FEE + plusFees };
    })
    .sort((a, b) => a.id - b.id)
    .map(({ fee }) => fee);
}
