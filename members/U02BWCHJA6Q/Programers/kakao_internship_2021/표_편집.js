// https://programmers.co.kr/learn/courses/30/lessons/81303

const JOB = Object.freeze({
  DOWN: 'D',
  UP: 'U',
  CUT: 'C',
  RESTORE: 'Z',
});

function Node(id) {
  this.id = id;
  this.prev = null;
  this.next = null;
}

function LinkedList(n) {
  this.head = null;
  this.current = null;
  this.deletedList = [];

  for (let i = 0; i < n; i++) {
    const node = new Node(i);

    if (this.head === null) {
      this.head = node;
      this.current = node;
    } else {
      this.current.next = node;
      node.prev = this.current;
      this.current = node;
    }
  }

  this.current = this.head;

  this.delete = () => {
    this.deletedList.push(this.current);

    const prev = this.current.prev;
    const next = this.current.next;

    if (prev !== null) {
      prev.next = next;
    } else {
      this.head = next;
    }
    if (next !== null) {
      next.prev = prev;
    }

    next === null ? (this.current = prev) : (this.current = next);
  };

  this.restore = () => {
    const restored = this.deletedList.pop();

    if (restored.prev) {
      restored.prev.next = restored;
    } else {
      this.head = restored;
    }
    if (restored.next) {
      restored.next.prev = restored;
    }
  };
}

function solution(n, k, cmd) {
  const linkedList = new LinkedList(n);

  for (let i = 0; i < k; i++) {
    linkedList.current = linkedList.current.next;
  }

  cmd.forEach(string => {
    const [job, count] = string.split(' ');

    switch (job) {
      case JOB.DOWN:
        {
          for (let i = 0; i < count; i++) {
            linkedList.current = linkedList.current.next;
          }
        }
        break;
      case JOB.UP:
        {
          for (let i = 0; i < count; i++) {
            linkedList.current = linkedList.current.prev;
          }
        }
        break;
      case JOB.CUT:
        {
          linkedList.delete();
        }
        break;
      case JOB.RESTORE: {
        linkedList.restore();
      }
    }
  });

  const answer = Array(n).fill('X');

  linkedList.current = linkedList.head;
  while (linkedList.current) {
    answer[linkedList.current.id] = 'O';
    linkedList.current = linkedList.current.next;
  }

  return answer.join('');
}
