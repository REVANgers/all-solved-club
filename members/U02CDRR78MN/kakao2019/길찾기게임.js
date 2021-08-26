function solution(nodeinfo) {
  var answer = [[]];

  const tree = {
    head: null,
    insert: (x, y, value) => {
      const newNode = {
        x,
        y,
        value,
        left: null,
        right: null,
      };

      if (!tree.head) {
        tree.head = newNode;
        return;
      }

      let current = tree.head;
      while (true) {
        if (x < current.x) {
          if (!current.left) {
            current.left = newNode;
            return newNode;
          }
          current = current.left;
        } else {
          if (!current.right) {
            current.right = newNode;
            return newNode;
          }
          current = current.right;
        }
      }
    },
    preorder: () => {
      const res = [];

      const dfs = (node) => {
        if (!node) {
          return;
        }

        res.push(node.value);

        dfs(node.left);
        dfs(node.right);
      };

      dfs(tree.head);

      return res;
    },
    postorder: () => {
      const res = [];

      const dfs = (node) => {
        if (!node) {
          return;
        }

        dfs(node.left);
        dfs(node.right);

        res.push(node.value);
      };

      dfs(tree.head);

      return res;
    },
  };

  nodeinfo
    .map((node, i) => [node, i + 1])
    .sort((a, b) => b[0][1] - a[0][1])
    .forEach(([[x, y], idx]) => {
      tree.insert(x, y, idx);
    });

  return [tree.preorder(), tree.postorder()];
}
