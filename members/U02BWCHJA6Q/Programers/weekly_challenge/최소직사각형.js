function solution(sizes) {
  const answer = 0;
  let maxWidth = 0;
  let maxHeigth = 0;

  sizes.forEach(([width, heigth], index) => {
    if (width > heigth) {
      if (width > maxWidth) {
        maxWidth = width;
      }

      if (heigth > maxHeigth) {
        maxHeigth = heigth;
      }

      return;
    }

    if (heigth > maxWidth) {
      maxWidth = heigth;
    }

    if (width > maxHeigth) {
      maxHeigth = width;
    }
  });

  return maxWidth * maxHeigth;
}
