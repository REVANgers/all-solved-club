// https://programmers.co.kr/learn/courses/30/lessons/81302

function solution(places) {
  const answer = [];
  const LENGTH = 5;

  places.forEach(place => {
    const peoples = [];

    for (let y = 0; y < LENGTH; y++) {
      for (let x = 0; x < LENGTH; x++) {
        if (place[y][x] === 'P') {
          peoples.push({ y, x });
        }
      }
    }

    for (let i = 0; i < peoples.length - 1; i++) {
      for (let j = i + 1; j < peoples.length; j++) {
        const { y: ay, x: ax } = peoples[i];
        const { y: by, x: bx } = peoples[j];

        const distance = Math.abs(ay - by) + Math.abs(ax - bx);

        if (distance > 2) {
          continue;
        }

        if (distance <= 1) {
          answer.push(0);

          return;
        }

        let minX, minY, maxX, maxY;

        if (ay < by) {
          minY = ay;
          maxY = by;
        } else {
          minY = by;
          maxY = ay;
        }

        if (ax < bx) {
          minX = ax;
          maxX = bx;
        } else {
          minX = bx;
          maxX = ax;
        }

        for (let y = minY; y <= maxY; y++) {
          for (let x = minX; x <= maxX; x++) {
            if (place[y][x] === 'O') {
              answer.push(0);

              return;
            }
          }
        }
      }
    }
    answer.push(1);
  });

  return answer;
}
