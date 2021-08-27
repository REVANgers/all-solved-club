function solution(k, room_number) {
  const mapping = new Map();

  return room_number.map((roomId) => {
    if (!mapping.has(roomId)) {
      mapping.set(roomId, roomId + 1);
      return roomId;
    }

    let nextRoomId = mapping.get(roomId);

    const disjoint = [];

    while (mapping.has(nextRoomId)) {
      disjoint.push(nextRoomId);
      nextRoomId = mapping.get(nextRoomId);
    }

    [...disjoint, nextRoomId].forEach((m) => mapping.set(m, nextRoomId + 1));

    return nextRoomId;
  });
}
