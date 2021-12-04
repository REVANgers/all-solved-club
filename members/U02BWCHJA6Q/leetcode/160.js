/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  const set = new Set();

  let a = headA;

  while (a) {
    set.add(a);
    a = a.next;
  }

  let b = headB;

  while (b) {
    if (set.has(b)) {
      return b;
    }
    b = b.next;
  }

  return null;
};
