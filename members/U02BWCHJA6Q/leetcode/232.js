var MyQueue = function () {
  this.q = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
  this.q.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
  return this.q.shift();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
  return this.q[0];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
  return this.q.length === 0;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
