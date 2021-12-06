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
var swapPairs = function (head) {
  let startRoot = new ListNode();
  startRoot.next = head;
  let current = startRoot;

  while (current.next && current.next.next) {
    const prev = current.next;
    const next = current.next.next;

    current.next.next = current.next.next.next;
    current.next = next;
    current.next.next = prev;

    current = current.next.next;
  }

  return startRoot.next;
};
