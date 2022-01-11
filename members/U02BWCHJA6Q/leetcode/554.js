/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function (wall) {
  const map = new Map();

  wall.forEach(bricks => {
    let edge = 0;

    for (let i = 0; i < bricks.length - 1; i++) {
      edge += bricks[i];

      map.set(edge, map.get(edge) + 1 || 1);
    }
  });

  let max = 0;
  for (let [edge, count] of map) {
    max = Math.max(max, count);
  }

  return wall.length - max;
};
