/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function (head, val) {
  const removedNode = new ListNode();

  let originalCurrent = head;
  let removedNodeCurrent = removedNode;

  while (originalCurrent) {
    if (originalCurrent.val !== val) {
      removedNodeCurrent.next = new ListNode(originalCurrent.val);
      removedNodeCurrent = removedNodeCurrent.next;
    }

    originalCurrent = originalCurrent.next;
  }

  return removedNode.next;
};
