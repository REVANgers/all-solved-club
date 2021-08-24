function solution(n, arr1, arr2) {
  var answer = [];

  return Array(n)
    .fill(0)
    .map((_, i) => {
      const col = Array(n).fill(0);

      let n1 = arr1[i];
      let n2 = arr2[i];

      let count = n - 1;

      while (count >= 0) {
        col[count] = (n1 % 2 || n2 % 2) === 1 ? "#" : " ";

        n1 = Math.floor(n1 / 2);
        n2 = Math.floor(n2 / 2);

        count--;
      }

      return col.join("");
    });

  return answer;
}
