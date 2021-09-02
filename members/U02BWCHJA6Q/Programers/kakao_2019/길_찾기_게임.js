// https://programmers.co.kr/learn/courses/30/lessons/42892

function Node({ y, x, id }) {
  this.id = id;
  this.y = y;
  this.x = x;
  this.left = null;
  this.right = null;
}

function BinaryTree() {
  this.root = null;

  this.add = (node, target) => {
    if (!target) {
      target = this.root;
    }

    if (target === null) {
      this.root = node;

      return;
    }

    const side = target.x > node.x ? 'left' : 'right';

    if (target[side] === null) {
      target[side] = node;
    } else {
      this.add(node, target[side]);
    }
  };

  this.preOrder = (node, result) => {
    result.push(node.id);

    if (node.left !== null) {
      this.preOrder(node.left, result);
    }
    if (node.right !== null) {
      this.preOrder(node.right, result);
    }
  };

  this.postOrder = (node, result) => {
    if (node.left !== null) {
      this.postOrder(node.left, result);
    }
    if (node.right !== null) {
      this.postOrder(node.right, result);
    }
    result.push(node.id);
  };
}

function solution(nodeinfo) {
  nodeinfo = nodeinfo.map(([x, y], index) => ({ x, y, id: index + 1 }));
  nodeinfo.sort(({ x: ax, y: ay }, { x: bx, y: by }) => {
    if (ay !== by) {
      return by - ay;
    }

    return ax - bx;
  });

  const binaryTree = new BinaryTree();

  nodeinfo.forEach(node => binaryTree.add(new Node(node)));

  const preOrderResult = [];
  const postOrderResult = [];

  binaryTree.preOrder(binaryTree.root, preOrderResult);
  binaryTree.postOrder(binaryTree.root, postOrderResult);

  return [preOrderResult, postOrderResult];
}
