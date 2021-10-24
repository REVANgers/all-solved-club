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
var reverseList = function (head) {
  const array = [];

  let current = head;

  while (current) {
    array.push(current.val);
    current = current.next;
  }

  const result = new ListNode();
  current = result;
  array.reverse().forEach(n => {
    current.next = new ListNode(n);
    current = current.next;
  });

  return result.next;
};
