function solution(id_list, report, k) {
  const reported = new Map();
  const reportList = new Map();

  id_list.forEach((id) => {
    reported.set(id, new Set());
    reportList.set(id, new Set());
  });

  report.forEach((string) => {
    const [from, to] = string.split(' ');

    reported.get(to).add(from);
    reportList.get(from).add(to);
  });

  return id_list.map(
    (id) =>
      [...reportList.get(id)].filter((_id) => reported.get(_id).size >= k)
        .length
  );
}
