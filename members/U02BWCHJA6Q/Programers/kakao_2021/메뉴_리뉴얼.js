// https://programmers.co.kr/learn/courses/30/lessons/72411

const courseMap = {};

const getCombinations = (array, number) => {
  const result = [];

  if (array.length < number) {
    return result;
  }

  if (number === 1) {
    return array.map(v => v);
  }

  array.forEach((fixed, index) => {
    const rest = array.slice(index + 1);
    const restCombinations = getCombinations(rest, number - 1);

    const combine = restCombinations.map(v => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
};

function solution(orders, course) {
  const answer = [];

  orders.forEach(order => {
    course.forEach(count => {
      const courseList = getCombinations(
        order.split('').sort(),
        count,
      ).map(course => course.join(''));
      courseList.forEach(course =>
        courseMap[course] ? (courseMap[course] += 1) : (courseMap[course] = 1),
      );
    });
  });

  const max = {};
  const courseList = Object.entries(courseMap).sort((a, b) => {
    if (a[0].length !== b[0].length) {
      return a[0].length - b[0].length;
    }

    return b[1] - a[1];
  });

  courseList.forEach(([course, count]) => {
    if (!max[course.length]) {
      max[course.length] = count;

      return;
    }

    if (max[course.length] < count) {
      max[course.length] = count;
    }
  });

  courseList.forEach(([course, count]) => {
    if (count === max[course.length] && count >= 2) {
      answer.push(course);
    }
  });

  return answer.sort();
}
