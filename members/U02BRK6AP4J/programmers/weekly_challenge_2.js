const makeScore = s => s >= 90 ? 'A' :
                       s >= 80 ? 'B' :
                       s >= 70 ? 'C' :
                       s >= 50 ? 'D' :
                       'F'
const sum = lst => lst.reduce((a, b) => a + b, 0)
const solution = scores => {
    return scores.reduce((a, b) => b.map((e, i) => [...a[i], e]), Array(scores.length).fill([])).map((e, i) => e.filter((e2, i2) => !( i === i2 && e.filter(v => v === Math.max(...e)).length === 1 && Math.max(...e) === e2 )).filter((e2, i2) => !( i === i2 && e.filter(v => v === Math.min(...e)).length === 1 && Math.min(...e) === e2 ) )).map(e => makeScore(sum(e) / e.length)).join('')
}