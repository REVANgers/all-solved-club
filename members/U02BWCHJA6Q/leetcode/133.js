/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {
  const map = new Map();

  const clone = node => {
    if (!node) {
      return null;
    }

    if (map.has(node.val)) {
      return map.get(node.val);
    }

    const cloned = new Node(node.val);
    map.set(node.val, cloned);
    cloned.neighbors = node.neighbors.map(neighbor => clone(neighbor));

    return cloned;
  };

  return clone(node);
};
