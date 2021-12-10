/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function (head, k) {
  let root = new ListNode();
  let current = head;
  let count = 0;
  let stack = [];

  while (count < k) {
    stack.push(current);

    if (!current.next) {
      current = null;
      break;
    }

    current = current.next;
    count++;
  }

  const tailNext = current;
  let prev = stack.pop();
  root.next = prev;

  while (stack.length > 0) {
    let next = stack.pop();

    prev.next = next;
    prev = next;
  }
  prev.next = tailNext;
  let tail = prev;

  while (current) {
    stack = [];
    count = 0;

    while (count < k) {
      stack.push(current);

      if (!current.next) {
        current = null;
        break;
      }

      current = current.next;
      count++;
    }

    if (stack.length < k) {
      break;
    }

    const tailNext = current;
    prev = stack.pop();
    tail.next = prev;

    while (stack.length > 0) {
      let next = stack.pop();

      prev.next = next;
      prev = next;
    }
    prev.next = tailNext;
    tail = prev;
  }

  return root.next;
};
