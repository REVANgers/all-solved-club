// 너무 느림, 다시 풀기

function solution(words, queries) {
  function Trie(type) {
    this.type = type;
    this.heads = new Map();
    this.search = (query) => {
      let current = this.heads.get(query.length);

      let i = this.type === "forward" ? 0 : query.length - 1;

      while (query[i] !== "?") {
        if (!current) {
          return 0;
        }

        current = current.keys.get(query[i]);

        i += this.type === "forward" ? 1 : -1;
      }

      return current ? current.weight : 0;
    };
    this.insert = (word) => {
      if (!this.heads.has(word.length)) {
        this.heads.set(word.length, {
          keys: new Map(),
          weight: 0,
        });
      }

      let current = this.heads.get(word.length);

      for (let i = 0; i < word.length; i++) {
        current.weight += 1;

        const c = this.type === "forward" ? word[i] : word[word.length - 1 - i];

        if (!current.keys.has(c)) {
          current.keys.set(c, {
            keys: new Map(),
            weight: 0,
          });
        }

        current = current.keys.get(c);
      }
    };
  }

  const forwardTrie = new Trie("forward");
  const reverseTrie = new Trie("reverse");

  words.forEach((word) => {
    forwardTrie.insert(word);
    reverseTrie.insert(word);
  });

  return queries.map((query) => {
    if (query[query.length - 1] === "?") {
      return forwardTrie.search(query);
    }
    if (query[0] === "?") {
      return reverseTrie.search(query);
    }
  });
}
