// https://programmers.co.kr/learn/courses/30/lessons/72410

const solution = new_id => {
  const processedId = new_id
    .toLowerCase()
    .replace(/[^\w\d-_.]/g, '')
    .replace(/\.{2,}/g, '.')
    .replace(/^\.|\.$/g, '')
    .padEnd(1, 'a')
    .slice(0, 15)
    .replace(/\.$/g, '');
  return processedId.padEnd(3, processedId[processedId.length - 1]);
};
