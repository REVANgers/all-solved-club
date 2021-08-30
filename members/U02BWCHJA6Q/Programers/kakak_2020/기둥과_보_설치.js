// https://www.welcomekakao.com/learn/courses/30/lessons/60061

let gidungList = [];
let boList = [];

const STRUCTURE_TYPE = Object.freeze({
  GIDUNG: 0,
  BO: 1,
});

const JOB = Object.freeze({
  REMOVE: 0,
  INSTALL: 1,
});

const isPossibleInstallGidung = (x, y) => {
  if (y === 0) {
    return true;
  }

  if (
    boList.some(
      ({ y: boY, x: boX }) => boY === y && (boX === x || boX + 1 === x),
    )
  ) {
    return true;
  }

  if (
    gidungList.some(
      ({ y: gidungY, x: gidungX }) => gidungY + 1 === y && gidungX === x,
    )
  ) {
    return true;
  }

  return false;
};

const isPossibleInstallBo = (x, y) => {
  if (
    gidungList.some(
      ({ y: gidungY, x: gidungX }) =>
        gidungY + 1 === y && (gidungX === x || gidungX === x + 1),
    )
  ) {
    return true;
  }

  const leftExist = boList.some(
    ({ y: boY, x: boX }) => y === boY && x === boX + 1,
  );
  const rightExist = boList.some(
    ({ y: boY, x: boX }) => y === boY && x + 1 === boX,
  );

  if (leftExist && rightExist) {
    return true;
  }

  return false;
};

const removeGidung = (x, y) => {
  const prevGidungList = gidungList;
  gidungList = gidungList.filter(
    ({ y: gidungY, x: gidungX }) => !(x === gidungX && y === gidungY),
  );

  const gidungOk = gidungList.every(({ y, x }) =>
    isPossibleInstallGidung(x, y),
  );
  const boOk = boList.every(({ y, x }) => isPossibleInstallBo(x, y));

  if (gidungOk && boOk) {
    return true;
  }

  gidungList = prevGidungList;

  return false;
};

const removeBo = (x, y) => {
  const prevBoList = boList;
  boList = boList.filter(({ y: boY, x: boX }) => !(x === boX && y === boY));
  const gidungOk = gidungList.every(({ y, x }) =>
    isPossibleInstallGidung(x, y),
  );
  const boOk = boList.every(({ y, x }) => isPossibleInstallBo(x, y));

  if (gidungOk && boOk) {
    return true;
  }

  boList = prevBoList;

  return false;
};

function solution(n, build_frame) {
  build_frame.forEach(([x, y, type, job]) => {
    if (type === STRUCTURE_TYPE.GIDUNG) {
      if (job === JOB.INSTALL) {
        if (isPossibleInstallGidung(x, y)) {
          gidungList.push({ y, x, type });
        }
      } else {
        removeGidung(x, y);
      }
    } else {
      if (job === JOB.INSTALL) {
        if (isPossibleInstallBo(x, y)) {
          boList.push({ y, x, type });
        }
      } else {
        removeBo(x, y);
      }
    }
  });

  return [...gidungList, ...boList]
    .sort((a, b) => {
      if (a.x !== b.x) {
        return a.x - b.x;
      }
      if (a.y !== b.y) {
        return a.y - b.y;
      }
      return a.type - b.type;
    })
    .map(({ x, y, type }) => [x, y, type]);
}
