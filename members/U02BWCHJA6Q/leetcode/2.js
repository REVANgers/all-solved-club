/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let carry = 0;
  let current1 = l1;
  let current2 = l2;
  const head = new ListNode();
  let result = head;

  while (current1 && current2) {
    const sum = current1.val + current2.val + carry;
    result.next = new ListNode(sum % 10);
    carry = (sum / 10) | 0;
    current1 = current1.next;
    current2 = current2.next;
    result = result.next;
  }

  if (current1) {
    while (current1) {
      const sum = current1.val + carry;
      result.next = new ListNode(sum % 10);
      carry = (sum / 10) | 0;
      current1 = current1.next;
      result = result.next;
    }
  }
  if (current2) {
    while (current2) {
      const sum = current2.val + carry;
      result.next = new ListNode(sum % 10);
      carry = (sum / 10) | 0;
      current2 = current2.next;
      result = result.next;
    }
  }

  if (carry > 0) {
    result.next = new ListNode(carry);
  }

  return head.next;
};
