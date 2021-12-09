/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function (n, k) {
  if (n === 1) {
    return 1;
  }

  let count = 0;
  let head = new Node(1);
  let current = head;

  for (let i = 1; i < n; i++) {
    current.next = new Node(i + 1);
    current = current.next;
  }
  current.next = head;

  while (count < n - 1) {
    current = head;
    let prev = current;

    for (let i = 0; i < k - 1; i++) {
      prev = current;
      current = current.next;
    }

    let next = current.next;
    prev.next = next;
    count++;

    head = next;
  }

  return head.data;
};

function Node(data) {
  this.data = data || -1;
  this.next = null;
}
