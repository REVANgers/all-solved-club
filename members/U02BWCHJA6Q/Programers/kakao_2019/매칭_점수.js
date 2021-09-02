// https://programmers.co.kr/learn/courses/30/lessons/42893

const PATTERN = Object.freeze({
  URL: /meta property=\"og:url\" content=\"https:\/\/(?<url>.*)\"\/>/,
  LINK: /<a href=\"https:\/\/(?<link>.*)\">/,
});

function solution(word, pages) {
  word = word.toLowerCase();

  const pageInformations = pages.map((page, index) => {
    const { url } = page.match(PATTERN.URL).groups;
    const links = [];
    page.split('</a>').forEach(string => {
      if (string.match(PATTERN.LINK)) {
        links.push(string.match(PATTERN.LINK).groups.link);
      }
    });

    const basicScore = page
      .split(/[^a-zA-Z]/)
      .filter(s => s.toLowerCase() === word).length;

    return { index, url, links, basicScore, matchScore: basicScore };
  });

  pageInformations.forEach(({ links, basicScore }) => {
    links.forEach(link => {
      pageInformations.some(page => {
        if (page.url === link) {
          page.matchScore += basicScore / links.length;

          return true;
        }
      });
    });
  });

  pageInformations.sort((a, b) => {
    if (a.matchScore !== b.matchScore) {
      return b.matchScore - a.matchScore;
    }

    return a.index - b.index;
  });

  return pageInformations[0].index;
}
