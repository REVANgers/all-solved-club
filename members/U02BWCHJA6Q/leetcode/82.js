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
  const set = new Set();
  const exist = new Set();

  let current = head;

  while (current) {
    if (exist.has(current.val)) {
      set.delete(current.val);
      current = current.next;

      continue;
    }

    set.add(current.val);
    exist.add(current.val);
    current = current.next;
  }

  const result = new ListNode();

  current = result;

  [...set].forEach(number => {
    current.next = new ListNode(number);
    current = current.next;
  });

  return result.next;
};
