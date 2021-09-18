// https://programmers.co.kr/learn/courses/30/lessons/64063

function Node(id, next) {
  this.id = id;
  this.next = next || null;
}

function solution(k, room_number) {
  const answer = [];
  const reservations = new Map();

  room_number.forEach(wanted => {
    if (!reservations.has(wanted)) {
      answer.push(wanted);
      reservations.set(
        wanted,
        new Node(wanted, reservations[wanted + 1] || new Node(wanted + 1)),
      );

      return;
    }

    let next = reservations.get(wanted).next;
    const beforeList = [reservations.get(wanted)];

    while (reservations.has(next.id)) {
      beforeList.push(next);
      next = reservations.get(next.id).next;
    }

    answer.push(next.id);
    reservations.set(next.id, next);

    const nextNext = new Node(next.id + 1);

    beforeList.forEach(node => (node.next = nextNext));
    next.next = nextNext;
  });

  return answer;
}
