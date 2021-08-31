const rotateKey = key => {
  const rotatedKey = [];

  for (let x = 0; x < key.length; x++) {
    const column = [];

    for (let y = key.length - 1; y >= 0; y--) {
      column.push(key[y][x]);
    }
    rotatedKey.push(column);
  }

  return rotatedKey;
};

const copyLock = lock => {
  const copiedLock = [];

  for (let column of lock) {
    copiedLock.push([...column]);
  }

  return copiedLock;
};

const isAllLocked = lock =>
  lock.every(column => column.every(current => current === 1));

const isPossibleLock = (y, x, key, lock) => {
  for (let keyY = 0; keyY < key.length; keyY++) {
    for (let keyX = 0; keyX < key.length; keyX++) {
      const nextY = keyY + y;
      const nextX = keyX + x;

      if (
        nextY < 0 ||
        nextX < 0 ||
        nextY >= lock.length ||
        nextY >= lock.length
      ) {
        continue;
      }

      if (
        (key[keyY][keyX] === 1 && lock[nextY][nextX] === 1) ||
        (key[keyY][keyX] === 0 && lock[nextY][nextX] === 0)
      ) {
        return false;
      }

      lock[nextY][nextX] = 1;
    }
  }

  return isAllLocked(lock);
};

function solution(key, lock) {
  let rotatedKey = key;

  for (let y = -(lock.length - 1); y < lock.length + (lock.length - 1); y++) {
    for (let x = -(lock.length - 1); x < lock.length + (lock.length - 1); x++) {
      for (let i = 0; i < 4; i++) {
        rotatedKey = rotateKey(rotatedKey);

        if (isPossibleLock(y, x, rotatedKey, copyLock(lock))) {
          return true;
        }
      }
    }
  }
  return false;
}
