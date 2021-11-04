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
var deleteDuplicates = function (head) {
  const result = new ListNode(Infinity);

  let current = head;
  let resultCurrent = result;

  while (current) {
    if (resultCurrent.val !== current.val) {
      resultCurrent.next = new ListNode(current.val);
      resultCurrent = resultCurrent.next;
    }
    current = current.next;
  }

  return result.next;
};
