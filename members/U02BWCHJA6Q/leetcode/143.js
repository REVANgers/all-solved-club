/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  let front = head;
  let tail = head;
  const stack = [];

  while (tail) {
    stack.push(tail);
    tail = tail.next;
  }

  if (front === tail) {
    return head;
  }

  while (front.next && front.next.next) {
    let frontNext = front.next;

    tail = stack.pop();
    stack[stack.length - 1].next = null;

    front.next = tail;
    tail.next = frontNext;

    front = frontNext;
  }

  return head;
};
