/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
  let count = 1;
  let next = head;
  while (next.next !== null) {
    next = next.next;
    count++;
  }
  const mid = (count / 2) | 0;

  for (let i = 0; i < mid; i++) {
    head = head.next;
  }

  return head;
};
