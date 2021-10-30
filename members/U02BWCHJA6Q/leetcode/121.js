/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let max = 0;
  let buy = prices[0];
  let sell = 0;

  for (let i = 1; i < prices.length; i++) {
    sell = prices[i];
    max = Math.max(max, sell - buy);

    if (buy > sell) {
      buy = sell;
    }
  }

  return max;
};
