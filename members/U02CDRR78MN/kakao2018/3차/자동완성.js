function solution(words) {
  var answer = 0;

  const trie = {
    root: {
      children: {},
    },

    add: (str) => {
      let i = 0;
      let current = trie.root;

      while (i < str.length) {
        const char = str[i];

        if (current.children[char]) {
          current.children[char].weight += 1;
        } else {
          current.children[char] = { children: {}, weight: 1 };
        }

        current = current.children[char];
        i++;
      }
    },
  };

  words.forEach((word) => trie.add(word));

  const getDepth = (word) => {
    let current = trie.root;
    let i = 0;

    while (true) {
      const char = word[i];

      if (current.children[char].weight === 1 || i === word.length - 1) {
        const depth = i + 1;

        return depth;
      }

      current = current.children[char];

      i++;
    }
  };

  return words
    .map((node) => getDepth(node))
    .reduce((acc, depth) => acc + depth);
}
