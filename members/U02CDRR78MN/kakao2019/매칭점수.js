// 9번 실패 케이스 해결하지 못 하고 포기..
function solution(word, pages) {
  var answer = 0;

  const pageInfo = {};

  const metaRegex =
    /<meta property="og:url" content="(?<url>https:\/\/[^"\s]+)"\/>/;
  const wordRegex = new RegExp(`(${word}){1,}`, "gi");
  const linkRegex = /<a href="https:\/\/[^"\s]+">/gi;

  pages.forEach((page, index) => {
    const url = page.match(metaRegex).groups.url;
    const words = (page.match(wordRegex) || []).filter(
      (repeated) => repeated.toLowerCase() === word.toLowerCase()
    );
    const links = (page.match(linkRegex) || []).map(
      (str) => str.match(/https:\/\/[^"\s]+/)[0]
    );

    pageInfo[url] = {
      index,
      baseScore: words.length,
      linkScore: words.length / links.length,
      links,
      linkedScore: 0,
    };
  });

  Object.values(pageInfo).forEach((page) => {
    page.links.forEach((linkURL) => {
      if (pageInfo[linkURL]) {
        pageInfo[linkURL].linkedScore += page.linkScore;
      }
    });
  });

  return Object.values(pageInfo)
    .map((page) => ({
      index: page.index,
      score: page.baseScore + page.linkedScore,
    }))
    .sort((a, b) =>
      a.score > b.score ? -1 : a.score < b.score ? 1 : a.index - b.index
    )[0].index;
}
